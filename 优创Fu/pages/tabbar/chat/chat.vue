<template>
  <view class="chat-container">
    <!-- 顶部标题 -->
    <view class="chat-header">
      <text class="title">聊天</text>
      <text class="icon" style="font-size: 24px;">&#128269;</text>
    </view>

    <!-- 标签页 -->
    <view class="tabs">
      <view :class="{'tab-active': activeTab === '消息'}" @tap="activeTab = '消息'">消息</view>
      <view :class="{'tab-active': activeTab === '添加好友'}" @tap="activeTab = '添加好友'">添加好友</view>
    </view>

    <!-- 消息列表 -->
    <scroll-view v-if="activeTab === '消息'" scroll-y="true" class="chat-list">
      <view class="chat-item" v-for="(message, index) in messages" :key="index" @tap="openChatDetail(message.name)">
        <view class="avatar-wrapper">
          <image v-if="message.avatar" :src="message.avatar" mode="aspectFill" class="avatar" />
          <view v-else class="system-icon">🔔</view>
          <!-- 消息提示红点 -->
          <view class="badge" v-if="message.unread > 0">{{ message.unread }}</view>
        </view>
        <view class="message-content">
          <view class="message-header">
            <text class="username">{{ message.name }}</text>
            <text class="time">{{ message.time }}分钟前</text>
          </view>
          <view class="message-text">{{ message.text }}</view>
        </view>
      </view>
    </scroll-view>

    <!-- 添加好友功能 -->
    <view v-if="activeTab === '添加好友'" class="add-friend-section">
      <input type="text" placeholder="输入用户名以搜索" v-model="searchQuery" @input="searchUsers" class="search-input" />
      <view v-if="searchResults.length > 0">
        <view class="result-item" v-for="(user, index) in searchResults" :key="index">
          <view class="username">{{ user.username }}</view>
          <button v-if="!isFriend(user.username)" @click="addFriend(user.username)" class="add-friend-btn">加好友</button>
          <text v-else class="already-friend">已是好友</text>
        </view>
      </view>
      <view v-if="searchResults.length === 0 && searchQuery">
        <text>未找到用户</text>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      activeTab: '消息', // 当前激活的选项卡
      searchQuery: '', // 用户输入的搜索用户名
      searchResults: [], // 搜索结果
      currentUser: 'Cypher', // 假设当前登录的用户
      friends: [], // 当前用户的好友列表
      messages: [
        {
          name: '系统消息',
          avatar: '',
          time: 1,
          text: '来自系统的消息',
          unread: 3
        },
        {
          name: 'Kobe',
          avatar: '/static/kobe.jpg', // 使用本地静态资源的路径
          time: 5,
          text: 'man!',
          unread: 6
        },
        {
          name: '马嘉祺',
          avatar: '/static/user2.jpg',
          time: 5,
          text: '对我们的项目有兴趣吗?',
          unread: 3
        }
      ]
    };
  },
  methods: {
    // 搜索用户功能
searchUsers() {
  if (this.searchQuery.trim() === '') {
    // 如果搜索框为空，清空搜索结果
    this.searchResults = [];
    return;
  }

  const users = uni.getStorageSync('users') || [];
  this.searchResults = users.filter(user => user.username.includes(this.searchQuery) && user.username !== this.currentUser);
},
    // 判断是否已经是好友
    isFriend(username) {
      return this.friends.includes(username);
    },
    // 添加好友功能
    addFriend(username) {
      const users = uni.getStorageSync('users') || [];
      const currentUser = users.find(user => user.username === this.currentUser);
      const friendUser = users.find(user => user.username === username);

      if (!currentUser.friends.includes(username)) {
        currentUser.friends.push(username); // 当前用户添加好友
        friendUser.friends.push(this.currentUser); // 好友也添加当前用户
        this.friends.push(username); // 更新本地好友列表
        uni.setStorageSync('users', users); // 保存到本地存储
        uni.showToast({
          title: '好友添加成功',
          icon: 'success'
        });
      } else {
        uni.showToast({
          title: '你们已经是好友了',
          icon: 'none'
        });
      }
    },
    // 打开聊天详情页面
    openChatDetail(username) {
      console.log('Navigating to chatDetail with username:', username);
      uni.navigateTo({
        url: `/pages/chatDetail/chatDetail?username=${encodeURIComponent(username)}`,
        success: () => {
          console.log('Navigation to chatDetail successful');
        },
        fail: (err) => {
          console.error('Navigation to chatDetail failed:', err);
          uni.showToast({
            title: '无法打开聊天页面',
            icon: 'none'
          });
        }
      });
    },

    // 加载当前用户的好友列表
    loadFriends() {
      const users = uni.getStorageSync('users') || [];
      const currentUser = users.find(user => user.username === this.currentUser);
      if (currentUser) {
        this.friends = currentUser.friends || [];
      }
    }
  },
  onShow() {
    this.loadFriends(); // 每次页面显示时加载好友列表
  }
};
</script>

<style scoped>
.chat-container {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.chat-header {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 16px;
  background-color: #fff;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1);
}

.chat-header .title {
  font-size: 24px;
  font-weight: bold;
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
}

.chat-header .icon {
  font-size: 24px;
  position: absolute;
  right: 16px;
  top: 50%;
  transform: translateY(-50%);
}

.tabs {
  display: flex;
  justify-content: space-around;
  background-color: #fff;
  padding: 12px;
  border-bottom: 1px solid #eee;
}

.tab-active {
  color: #f7a300;
  border-bottom: 2px solid #f7a300;
}

.chat-list {
  flex-grow: 1;
  overflow-y: auto;
  padding: 20rpx;
  background-color: #f9f9f9;
}

.chat-item {
  display: flex;
  align-items: center;
  padding: 10px;
  margin-bottom: 10px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  cursor: pointer; /* 添加指针样式 */
  margin-right: 40rpx;
}

.avatar-wrapper {
  position: relative;
  width: 40px;
  height: 40px;
}

.avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
}

.system-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #eee;
  display: flex;
  align-items: center;
  justify-content: center;
}

.badge {
  position: absolute;
  top: -5px;
  right: -5px;
  width: 18px;
  height: 18px;
  background-color: #f44336;
  color: white;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 12px;
}

.message-content {
  flex-grow: 1;
  margin-left: 10px;
}

.message-header {
  display: flex;
  justify-content: space-between;
}

.username {
  font-weight: bold;
}

.time {
  color: #aaa;
}

.message-text {
  color: #333;
}

.add-friend-section {
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.search-input {
  width: 100%;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #dcdcdc;
  margin-bottom: 20px;
}

.result-item {
  display: flex;
  align-items: center;
  justify-content: space-between; /* 让左右两侧对齐 */
  padding: 10px;
  border-bottom: 1px solid #eee;
}

.add-friend-btn {
  background-color: #00bcd4;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 15px;
  cursor: pointer;
  /* 去掉 margin-left: auto; */
}

.already-friend {
  color: #888;
  margin-left: auto; /* 让 "已是好友" 也右对齐 */
}
</style>
