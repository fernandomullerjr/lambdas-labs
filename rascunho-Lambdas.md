

git status
eval $(ssh-agent -s)
ssh-add /home/fernando/.ssh/chave-debian10-github
git add .
git commit -m "Lambda em Python - Tratamento de JSON"
git push
git status