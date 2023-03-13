import openai

#filename = './data/程式語言_Week3_Python基礎02.txt'
filename = './data/web3talk.txt'

with open(filename, 'r', encoding='utf-8') as fh:
    tmp = fh.read()
    itemlist = tmp.split(',')


itemlist = str(itemlist)

keyfile = open("key.txt", "r")
key = keyfile.readline()

openai.api_key = key

start_idx = 0
result = ''
while start_idx < len(itemlist):
    end_idx = min(start_idx + 1600, len(itemlist))
    sub_list = itemlist[start_idx:end_idx]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": f"將這些對話變成一篇以 Pecu 的口氣寫的中文文章：{sub_list}"}
        ]
    )

    print(start_idx)

    for choice in response.choices:
        result += choice.message.content
    start_idx = end_idx

with open('output.txt', 'w', encoding='utf-8') as output_file:
    print(result)
    output_file.write(result)