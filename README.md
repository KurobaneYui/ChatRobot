# ChatRobot
A chat bot for querying stock information on WeChat.


# Environment required
Rasa or Rasa-X
Spacy
python-mysql-connector

# Environment Install step
### use requirements.txt in /ChatRobot/whls/
pip install -r requirements.txt
### install additional package: Rasa or Rasa-X
1. python -m spacy download en_core_web_md //再利用spacy下载en_core_web_md
2. python -m spacy link en_core_web_md en //如果要在rasa中使用，记得链接至en
### download Spacy english word-module
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple //再安装rasa
