<template>
  <view class="chat-detail-container">
    <!-- 顶部标题 -->
    <view class="chat-detail-header">
      <text class="title">{{ contactName }}</text>
    </view>

    <!-- 消息列表 -->
    <scroll-view scroll-y="true" class="messages-list" :scroll-into-view="scrollToView">
      <view
        class="message-item"
        v-for="(msg, index) in messages"
        :key="index"
        :id="'msg-' + index" <!-- 添加唯一 id -->
        :class="{'sent': msg.sender === currentUser, 'received': msg.sender !== currentUser}"
      >
        <text class="message-text">{{ msg.text }}</text>
        <text class="message-time">{{ msg.time }}</text>
      </view>
    </scroll-view>

    <!-- 输入框和发送按钮 -->
    <view class="input-section">
      <input type="text" v-model="newMessage" placeholder="输入消息" class="message-input" @confirm="sendMessage" />
      <button @click="sendMessage" class="send-button">发送</button>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      contactName: '', // 聊天对象的用户名
      currentUser: 'Cypher', // 当前用户
      messages: [], // 当前聊天的消息列表
      newMessage: '', // 新消息内容
      scrollToView: ''
    };
  },
  methods: {
    // 加载聊天消息
    loadMessages() {
      const allMessages = uni.getStorageSync('chatMessages') || {};
      const key = this.getChatKey(this.currentUser, this.contactName);
      this.messages = allMessages[key] || [];
      this.scrollToBottom();
    },
    // 发送消息
    sendMessage() {
      if (this.newMessage.trim() === '') return;

      console.log('Sending message:', this.newMessage);
      const newMsg = {
        sender: this.currentUser,
        text: this.newMessage.trim(),
        time: this.getCurrentTime()
      };

      this.messages.push(newMsg);
      this.newMessage = '';
      this.saveMessages();
      this.scrollToBottom();

      // 模拟对方回复（可选）
      setTimeout(() => {
        const replyMsg = {
          sender: this.contactName,
          text: '收到您的消息',
          time: this.getCurrentTime()
        };
        this.messages.push(replyMsg);
        this.saveMessages();
        this.scrollToBottom();
      }, 1000);
    },
    // 保存消息到本地存储
    saveMessages() {
      const allMessages = uni.getStorageSync('chatMessages') || {};
      const key = this.getChatKey(this.currentUser, this.contactName);
      allMessages[key] = this.messages;
      uni.setStorageSync('chatMessages', allMessages);
    },
    // 获取聊天的唯一键
    getChatKey(user1, user2) {
      return [user1, user2].sort().join('_');
    },
    // 获取当前时间字符串
    getCurrentTime() {
      const now = new Date();
      const hours = now.getHours().toString().padStart(2, '0');
      const minutes = now.getMinutes().toString().padStart(2, '0');
      return `${hours}:${minutes}`;
    },
    // 滚动到最新消息
    scrollToBottom() {
      this.$nextTick(() => {
        if (this.messages.length > 0) {
          this.scrollToView = 'msg-' + (this.messages.length - 1);
        }
      });
    }
  },
  onLoad(options) {
    console.log('chatDetail onLoad options:', options);
    this.contactName = options.username;
    this.loadMessages();
  },
  watch: {
    messages() {
      this.scrollToBottom();
    }
  }
};
</script>

<style scoped>
.chat-detail-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.chat-detail-header {
  padding: 16px;
  background-color: #fff;
  border-bottom: 1px solid #eee;
  text-align: center;
}

.chat-detail-header .title {
  font-size: 20px;
  font-weight: bold;
}

.messages-list {
  flex-grow: 1;
  padding: 10px;
  background-color: #f9f9f9;
}

.message-item {
  max-width: 70%;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 8px;
  position: relative;
}

.message-item.sent {
  align-self: flex-end;
  background-color: #dcf8c6;
}

.message-item.received {
  align-self: flex-start;
  background-color: #fff;
}

.message-text {
  font-size: 16px;
  color: #333;
}

.message-time {
  font-size: 12px;
  color: #999;
  position: absolute;
  bottom: -15px;
  right: 10px;
}

.input-section {
  display: flex;
  padding: 10px;
  background-color: #fff;
  border-top: 1px solid #eee;
}

.message-input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #dcdcdc;
  border-radius: 20px;
  outline: none;
}

.send-button {
  margin-left: 10px;
  background-color: #00bcd4;
  color: white;
  border: none;
  border-radius: 20px;
  padding: 10px 20px;
  cursor: pointer;
}
</style>
