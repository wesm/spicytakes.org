# Spicy Takes Makefile

.PHONY: parquet dev deploy-landing deploy-landing-preview clean

# Build the analytics parquet file from all blog data
parquet:
	@echo "Building analytics parquet file..."
	python scripts/build_analytics_parquet.py

# Run the landing page dev server (builds parquet first)
dev: parquet
	VITE_BLOG_ID=landing npm run dev

# Deploy landing page to production (builds parquet first)
deploy-landing: parquet
	./scripts/deploy.sh landing --prod

# Deploy landing page preview (builds parquet first)
deploy-landing-preview: parquet
	./scripts/deploy.sh landing

# Clean generated files
clean:
	rm -f static/data/analytics_quotes.parquet
	rm -rf .svelte-kit build
