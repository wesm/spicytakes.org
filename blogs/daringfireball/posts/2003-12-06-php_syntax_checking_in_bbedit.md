---
title: "PHP Syntax Checking in BBEdit"
date: 2003-12-06
url: https://daringfireball.net/2003/12/php_syntax_checking_in_bbedit
slug: php_syntax_checking_in_bbedit
word_count: 1725
---


As mentioned a few months [ago](https://daringfireball.net/2003/04/command_line_fun), recent versions of PHP include a command-line tool, which means you can use PHP as a shell scripting language. The version of PHP that comes with Panther includes the PHP command-line tool; if you’re using Jaguar, you can download a free [PHP installer from Marc Liyanage](http://www.entropy.ch/software/macosx/php/) that includes command-line support.


Let’s put it to use, by adding PHP syntax checking to BBEdit.


Here’s how it works. If you pass the `php` command-line tool the `-l` option (that’s a lowercase L), it will perform a rudimentary syntax check instead of executing the source code. For example, from the terminal, you’d type:


```
php -l /path/to/your/file.php

```


I say “rudimentary” because, as far as I can tell, PHP’s syntax checker only detects parse errors — errors so egregious they cause PHP to be unable to parse the code. Also, because PHP stops processing the file once it hits a single parse error, it only returns a single error; if you’ve got multiple parse errors in your source code, PHP’s syntax checker will only gripe about the first one. You’ll need to fix it and re-run the checker to find the next one. Still, it’s better than no checker at all.


According to [PHP’s documentation for the `-l` switch](http://www.php.net/manual/en/features.commandline.php#AEN7401):


> This option provides a convenient way to only perform a syntax check on
> the given PHP code. On succes, the text `No syntax errors detected in
> <filename>` is written to standard output and the shell return code is
> `0`. On failure, the text `Errors parsing <filename>` in addition to
> the internal parser error message is written to standard output and the
> shell return code is set to `255`.


OK, so now we know how to tell the command-line `php` tool to perform a syntax check, and we know what kind of output to expect. To invoke it from BBEdit, we can use AppleScript’s `do shell script` command. So the basic gist of how the AppleScript script could work:

1. Get the path to the document of the front text window.
2. Use `do shell script` to call `php -l` followed by the path from step 1.
3. If there are no errors, put up a “No errors found” alert;
if a parse error is found, show the error message in an alert.


However, step 1, as stated above, is a bit lazy. What if the front BBEdit window has unsaved changes? We *could* have the script save the file automatically if it has unsaved changes. But that’s still lazy — we should be able to syntax-check a file with unsaved changes. Plus, what if the front BBEdit window is an untitled new document that’s never been saved?


One way to solve these problems is to use a temporary file if the front BBEdit window has unsaved changes (or if it’s not using Unix-style line endings, since that’s what the `php` tool expects). Then we’ll pass the temp file to PHP’s syntax checker.


When an error is found, we could create a BBEdit results browser window instead of simply displaying the error message in an alert. BBEdit does this with its built-in HTML syntax checker and with its support for syntax-checking Perl scripts. But what would be the point, since PHP is only ever going to return a single error at a time? A simple alert is less intrusive:


What *would* be a nice extra touch, however, would be checking to see if PHP returns a line number with the error message, and if so, selecting that line in the text window. So we’ll do that.


And, speaking of BBEdit’s built-in HTML checker, wouldn’t it be nice if we could combine it with our PHP checker? Because BBEdit supports script *attachability*, we can. By adding a short `menuselect()` handler to our script, we can use it as a BBEdit menu script.


Menu scripts are saved in the “Menu Scripts” folder in the “BBEdit Support” folder. Menu scripts can replace or supplement any of BBEdit’s built-in menu commands. Menu scripts are attached to commands by giving them special file names, in the form *Menu•Name*. In this case, because we want to supplement BBEdit’s HTML syntax checker, we need to use the file name “Check•Document Syntax”.


But we can also use the same script as a regular script, invoked from BBEdit’s Scripts menu. To do so, we’ll add an `on run` handler to the script.


Here’s how I have it set up here:

1. I saved the script as a compiled AppleScript, in the “Scripts”
folder in my “BBEdit Support Folder. I gave it the name “PHP
Syntax Check”, and that’s how it appears in my Scripts menu.
2. I made an alias to the “PHP Syntax Check” script, and I named
the alias “Check•Document Syntax”. I moved the alias to the
“Menu Scripts” folder.


So it’s just one script file, but with the use of an alias and two separate AppleScript handler routines, it can be used in two different ways:

- When it’s called normally, via the Scripts menu, the script’s
`on run` handler is invoked, and the only thing it does is
perform a PHP syntax check against the front window.
- When you invoke BBEdit’s Check Document Syntax command from the
Markup menu, the script’s `menuselect()` handler is invoked. If
PHP returns a parse error, we display the error message in an
alert and tell BBEdit not to perform the HTML syntax check. If
PHP does *not* find any errors, we tell BBEdit to perform its
HTML syntax check. Thus, if BBEdit displays its “No errors were
found” dialog, we know that the file passed through both syntax
checkers without complaint.


Here’s the script, with inline comments to explain the details:


```
-- start script
on run
   -- The run handler is called when the script is invoked normally,
   -- such as from BBEdit's Scripts menu.
   set php_errs to PHPSyntaxCheck()
   if not php_errs then
      display dialog "No PHP syntax errors detected." buttons {"OK"} ¬
         default button 1 with icon note
   end if
end run


on menuselect()
   -- The menuselect() handler gets called when the script is invoked
   -- by BBEdit as a menu script. Save this script, or an alias to it,
   -- as "Check•Document Syntax" in the "Menu Scripts" folder in your
   -- "BBEdit Support" folder.
   set php_errs to PHPSyntaxCheck()
   if php_errs then
      -- PHP reported an error, so tell BBEdit *not* to
      -- continue with it's HTML syntax check:
      return true
   else
      -- No PHP errors, so tell BBEdit to run its
      -- HTML syntax check 
      return false
   end if
end menuselect


on PHPSyntaxCheck()
   -- Input: none
   -- Returns: true if PHP reports errors, false otherwise

   tell application "BBEdit"
      try
         set w to text window 1
      on error
         beep
         return
      end try

        set is_dirty to modified of (document of w)
        -- Find out if w is using Mac, Unix, or DOS line endings:
        set linebreaks to (line breaks of document of w)
        set the_filename to name of (document of w)

      if (is_dirty) or (linebreaks is not equal to Unix) then
         -- We need to write a temporary file.
         set parent_folder to (path to temporary items folder)
         set temp_file to (parent_folder as string) & the_filename
         if not (my WriteUnixTextFile(temp_file, text of w)) then
            -- End script, because an error occured writing the temp file
            return
         end if
      else
         -- We can pass the actual file to PHP, no temp file needed:
         tell application "Finder"
            set parent_folder to (container of (file of w as alias)) as alias
         end tell
      end if
   end tell

   -- First, cd to the directory where the script file is, then tell
   -- php to syntax check it. We *could* do this with one command,
   -- by passing to php the full path of the script, but then the
   -- error messages from php will contain the full path as well,
   -- instead of just the file name.
   --
   -- (NOTE: If you're running Jaguar, you'll need to change the path for
   -- the php tool, probably to "/usr/local/php/bin/php" )
   set the_command to "cd " & quoted form of POSIX path of parent_folder & ¬
      ";  /usr/bin/php -l " & (quoted form of (the_filename))
   try
      set the_result to do shell script the_command
      if the_result starts with "No syntax errors detected" then
         set errors_found to false -- the return value
      else
         -- I don't think we'll ever get here, because if PHP reports
         -- any actual errors, they're sent to STDERR, not STDOUT, and
         -- will thus trigger the below 'on error' handler.
         display dialog the_result
      end if

   on error err_text
      tell application "BBEdit"
         try
            -- first line of err_text is, as far as I can tell, always blank
            -- second line is the useful error message
            -- third line is "Errors parsing <filename>"
            set errors_found to true
            set msg to paragraph 2 of err_text
            set line_num to last word of msg as integer
            select line line_num of text window 1
            display dialog "PHP " & msg with icon stop ¬
               buttons {"OK"} default button 1
         on error
            -- If the error message from PHP comes back in
            -- in an unexpected format, display it in a new
            -- BBEdit window.
            make new text window with properties {text:err_text}
         end try
      end tell
   end try

   return errors_found

end PHPSyntaxCheck



on WriteUnixTextFile(file_name, file_contents)
   -- Write a text file with unix-style line endings.
   -- Input:
   --    file_name - the HFS-style path for the file to write
   --    file_contents - the text to write to a file
   -- Returns: true for success, false for failure
   try
      set file_ref to ¬
         open for access file file_name with write permission
      set eof of file_ref to 0

      -- change the text of file_contents to unix line breaks
      set old_delims to AppleScript's text item delimiters
      set AppleScript's text item delimiters to return
      set text_list to every text item of file_contents as list
      set AppleScript's text item delimiters to (ASCII character 10)
      set file_contents to (text_list as string)
      set AppleScript's text item delimiters to old_delims

      write file_contents to file_ref starting at eof
      close access file_ref
      return true
   on error err_msg
      try
         close access file file_ref
      end try
      display dialog err_msg with icon stop buttons {"OK"} ¬
         default button 1
      return false
   end try
end WriteUnixTextFile
-- end script

```



| **Previous:** | [Graphic Communication](https://daringfireball.net/2003/12/graphic_communication) |
| **Next:** | [Old Habits](https://daringfireball.net/2003/12/old_habits) |


PreviousNext