from yunhu2onebot12 import Converter

# 创建转换器实例
converter = Converter()

message = {
  "version": "1.0",
  "header": {
    "eventId": "c192ccc83d5147f2859ca77bcfafc9f9",
    "eventType": "message.receive.normal",
    "eventTime": 1748613099002
  },
  "event": {
    "sender": {
      "senderId": "6300451",
      "senderType": "user",
      "senderUserLevel": "owner",
      "senderNickname": "ShanFish"
    },
    "chat": {
      "chatId": "49871624",
      "chatType": "bot"
    },
    "message": {
      "msgId": "5c887bc0a82244c7969c08000f5b3ae8",
      "parentId": "",
      "sendTime": 1748613098989,
      "chatId": "49871624",
      "chatType": "bot",
      "contentType": "text",
      "content": {
        "text": "你好"
      }
    }
  }
}

# 创建转换器对象
convert = Converter().convert

print(message)
print("---" * 10 + "转换结果" + "---" * 10)
print(convert(message))