<template>
  <view class="container">
    <!-- 用户头像部分 -->
    <view class="profile-avatar">
      <image :src="avatarUrl" class="avatar" @click="changeAvatar" />
      <text class="change-avatar-text">点击更换头像</text>
    </view>

    <!-- 修改用户名 -->
    <view class="form-section">
      <text class="label">用户名</text>
      <input v-model="username" type="text" placeholder="输入新的用户名" class="input" />
    </view>

    <!-- 修改详细信息 -->
    <view class="form-section">
      <text class="label">详细信息</text>
      <textarea v-model="details" placeholder="输入详细信息" class="input textarea"></textarea>
    </view>

    <!-- 保存按钮 -->
    <button class="save-btn" @click="saveChanges">保存修改</button>
  </view>
</template>

<script>
export default {
  data() {
    return {
      avatarUrl: '/static/default-avatar.png', // 默认头像路径
      username: '', // 用户名
      details: '', // 详细信息
    };
  },
  onShow() {
    this.loadUserInfo(); // 加载用户信息
  },
  methods: {
    // 加载本地存储的用户信息
    loadUserInfo() {
      const user = uni.getStorageSync('currentUser') || {
        avatarUrl: '/static/default-avatar.png',
        username: '默认用户',
        details: '这里是用户的详细信息'
      };
      this.avatarUrl = user.avatarUrl;
      this.username = user.username;
      this.details = user.details;
    },
    // 上传头像
    changeAvatar() {
      uni.chooseImage({
        count: 1, // 只能选择一张图片
        sizeType: ['original', 'compressed'], // 可以选择原图或压缩图
        sourceType: ['album', 'camera'], // 从相册或摄像头中选择
        success: (res) => {
          // 获取临时文件路径
          const tempFilePath = res.tempFilePaths[0];
          this.avatarUrl = tempFilePath; // 更新头像显示
        },
        fail: (err) => {
          console.error("头像更换失败：", err);
        }
      });
    },
    // 保存用户信息到本地存储
    saveChanges() {
      const updatedUser = {
        avatarUrl: this.avatarUrl,
        username: this.username,
        details: this.details
      };
      uni.setStorageSync('currentUser', updatedUser); // 将修改后的信息存储到本地
      uni.showToast({
        title: '修改成功',
        icon: 'success'
      });
    }
  }
};
</script>

<style scoped>
.container {
  width: 100%;
  height: 100vh;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #f9f9f9;
}

.profile-avatar {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  margin-bottom: 10px;
}

.change-avatar-text {
  font-size: 14px;
  color: #555;
}

.form-section {
  width: 80%;
  margin-bottom: 20px;
}

.label {
  display: block;
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}

.input {
  width: 100%;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ddd;
  background-color: #fff;
}

.textarea {
  height: 100px;
  resize: none;
}

.save-btn {
  width: 80%;
  height: 45px;
  background-color: #00bcd4;
  color: white;
  border-radius: 25px;
  font-size: 16px;
  text-align: center;
  line-height: 45px;
  cursor: pointer;
  border: none;
}
</style>
