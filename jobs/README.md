# Run these two first
	export FLASK_ENV=development
	export FLASK_APP=jobs


# Then run
	flask initdb
	flask crawl
	flask run
