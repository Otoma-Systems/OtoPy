python setup.py sdist
python setup.py bdist_wheel --universal
git add -A
set /p commitMessege=Commit messege?:
git commit -m %commitMessege%
git push