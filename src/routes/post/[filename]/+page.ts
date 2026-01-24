import type { PageLoad } from './$types';

export const load: PageLoad = ({ params, data }) => {
  return {
    filename: params.filename,
    post: data.post
  };
};
