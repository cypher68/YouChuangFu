<template>
  <view class="container">
    <!-- 顶部部分，包括LOGO和设置图标 -->
    <view class="header">
      <text class="logo">优创Fu</text>
      <!-- 绑定点击事件，点击设置图标跳转到登录页面 -->
      <image src="/static/setting.png" class="settings-icon" @click="goToSettings"></image>
    </view>

    <!-- 分割线：位于LOGO和头像之间 -->
    <view class="divider"></view>

    <!-- 用户头像和信息部分 -->
    <view class="profile-section">
      <image :src="avatarUrl" class="avatar"></image>
      <view class="user-info">
        <text class="username">{{ username }}</text>
        <text class="account">账号: {{ account }}</text> <!-- 显示登录时的账号信息 -->
      </view>
    </view>

    <!-- 提示信息部分 -->
    <view class="add-friend">
      <text>添加交友名片，找志同道合的朋友更方便</text>
    </view>

    <!-- 数据统计部分 -->
    <view class="stats">
      <view class="stat-item">
        <text class="stat-number">8</text>
        <text class="stat-label">获赞</text>
      </view>
      <view class="stat-item">
        <text class="stat-number">24</text>
        <text class="stat-label">关注</text>
      </view>
      <view class="stat-item">
        <text class="stat-number">16</text>
        <text class="stat-label">足迹</text>
      </view>
      <view class="stat-item">
        <text class="stat-number">4</text>
        <text class="stat-label">粉丝</text>
      </view>
    </view>

    <!-- 分割线：位于数据统计部分和按钮部分之间 -->
    <view class="divider"></view>

    <!-- 项目按钮部分 -->
    <view class="button-container">
      <button class="project-button" @click="goToPublish">发布项目</button>
      <button class="project-button" @click="goToJoinProject">加入项目</button>
      <button class="project-button" @click="MyProject">我的项目</button>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      username: '', // 初始化为空，稍后从存储中获取
      avatarUrl: '/static/avatar.png', // 默认头像
      account: '' // 账号信息初始化为空
    };
  },
  onShow() {
    this.loadUserInfo(); // 页面显示时加载用户信息
  },
  methods: {
    // 加载本地存储中的用户信息
    loadUserInfo() {
      const user = uni.getStorageSync('currentUser') || {
        username: '未登录用户',
        avatarUrl: '/static/avatar.png',
        account: '未登录'
      };
      this.username = user.username; // 更新用户名
      this.avatarUrl = user.avatarUrl; // 更新头像
      this.account = user.username; // 使用登录时的用户名作为账号
    },
    goToSettings() {
      uni.navigateTo({
        url: '/pages/login/login' // 设置跳转到登录页面的路径
      });
    },
    goToJoinProject() {
      uni.switchTab({
        url: '/pages/tabbar/project/project'
      });
    },
    goToPublish() {
      uni.navigateTo({
        url: '/pages/pulish/pulish' // 这里填写你的发布项目页面路径
      });
    },
    MyProject() {
      uni.navigateTo({
        url: '/pages/myproject/myproject' // 这里填写你的项目页面路径
      });
    }
  }
};
</script>

<style scoped>
/* 样式保持不变 */
.container {
  width: 100vw;
  height: 100vh;
  background-color: #012C54;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  box-sizing: border-box;
}

/* 顶部部分，显示LOGO和设置图标 */
.header {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  padding: 0 10px;
}

.logo {
  color: white;
  font-size: 20px;
  font-weight: bold;
}

.settings-icon {
  position: absolute;
  right: 10px;
  width: 24px;
  height: 24px;
  cursor: pointer;
}

/* 用户头像和信息部分 */
.profile-section {
  width: 90%;
  display: flex;
  align-items: center;
  margin-top: 20px;
}

.avatar {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  margin-right: 15px;
}

.user-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.username {
  color: white;
  font-size: 25px;
  font-weight: bold;
  margin-left: 20rpx;
}

.account {
  color: white;
  font-size: 16px;
  margin-top: 5px;
  margin-left: 30px;
}

.divider {
  width: 95%;
  height: 1px;
  background-color: rgba(255, 255, 255, 0.5);
  margin-top: 13px;
}

.add-friend {
  background-color: rgba(255, 255, 255, 0.2);
  padding: 10px;
  border-radius: 20px;
  text-align: center;
  color: white;
  font-size: 14px;
  margin: 20px 0;
  width: 80%;
}

.stats {
  display: flex;
  justify-content: space-around;
  width: 90%;
  margin-bottom: 20px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-number {
  font-size: 18px;
  color: white;
  font-weight: bold;
}

.stat-label {
  font-size: 12px;
  color: white;
}

.button-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 80%;
  margin-top: 30px;
}

.project-button {
  background-color: white;
  color: #012C54;
  padding: 6px 30px;
  font-size: 18px;
  border-radius: 30px;
  border: none;
  text-align: center;
  font-weight: bold;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  width: 100%;
}
</style>
