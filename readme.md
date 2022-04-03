A website with a custom made CRM. It includes the possibility of adding content from an administration dashboard.


# Run locally

python3 -m venv venv

venv/scripts/activate

pip install pipenv

pipenv install

SQLALCHEMY_DATABASE_URI=postgresql://postgres:postgres@localhost:5432/forcewing
