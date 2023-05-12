

git status
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git add .
git commit -m "Lambda Labs - JSON 2 HTML"
git push
git status