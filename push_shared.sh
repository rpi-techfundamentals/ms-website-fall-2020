#cp /Users/jasonkuruzovich/Box/Documents/Into-ml-app/book_fall_2020.xlsx   ./book.xlsx
source build.sh
ghp-import -n -p -f quant/_build/html
git add --all
if [ -z "$1"]
then
	git commit -m "push to public"
else
	git commit -m "$1"
fi
git push
