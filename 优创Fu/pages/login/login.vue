<template>
  <view class="container">
    <view class="logo">
      <image src="/static/logo.png" class="logo-image"></image>
    </view>
    <view class="form">
      <input v-model="username" type="text" placeholder="输入账号" class="input" />

      <!-- 密码输入框部分，带有查看密码的图标 -->
      <view class="input-wrapper">
        <input :type="passwordFieldType" v-model="password" placeholder="请输入密码" autocomplete="off" class="input" />
        <text @click="togglePasswordVisibility" class="eye-icon">{{ passwordVisible ? '🙈' : '👁️' }}</text>
      </view>

      <view class="forgot-password">
        <text>忘记密码?</text>
      </view>
      <button class="login-btn" @click="login">登录</button>
      <button class="register-btn" @click="goToRegister">注册</button>
    </view>
    <view class="agreement">
      <input type="checkbox" id="agreement" class="checkbox" />
      <label for="agreement" class="label-text">
        登录/注册表示您同意《用户协议》和《隐私政策》
      </label>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      passwordVisible: false // 控制密码可见性
    };
  },
  computed: {
    // 动态计算输入框的类型，根据 passwordVisible 控制显示/隐藏密码
    passwordFieldType() {
      return this.passwordVisible ? 'text' : 'password';
    }
  },
  methods: {
    // 切换密码的显示与隐藏
    togglePasswordVisibility() {
      this.passwordVisible = !this.passwordVisible;
    },
    login() {
      if (!this.username || !this.password) {
        uni.showToast({
          title: '请输入账号和密码',
          icon: 'none'
        });
        return;
      }

      // 发起 GET 请求到服务器，获取用户信息
      uni.request({
        url: `http://ci86ph16222.vicp.fun/findUser/?username=${encodeURIComponent(this.username)}`,
        method: 'GET',
        success: (res) => {
          console.log(res); // 打印服务器返回的完整响应

          if (res.statusCode === 200 && res.data && res.data.data.length > 0) {
            const serverPassword = res.data.data[0].password; // 获取服务器返回的密码

            // 进行密码比较
            if (this.password === serverPassword) {
              uni.showToast({
                title: '登录成功',
                icon: 'success'
              });

              // 保存当前用户信息到本地存储
              uni.setStorageSync('currentUser', { username: this.username, avatarUrl: '/static/avatar.png' });

              // 延迟1秒后跳转到 index 页面
              setTimeout(() => {
                uni.switchTab({
                  url: '/pages/tabbar/index/index'
                });
              }, 1000);
            } else {
              uni.showToast({
                title: '密码错误',
                icon: 'none'
              });
            }
          } else {
            uni.showToast({
              title: '用户不存在',
              icon: 'none'
            });
          }
        },
        fail: (err) => {
          uni.showToast({
            title: '请求失败，请检查网络连接',
            icon: 'none'
          });
          console.error('请求失败：', err);
        }
      });
    },
    // 注册按钮点击跳转到注册页面
    goToRegister() {
      uni.navigateTo({
        url: '/pages/signup/signup' // 确保你有这个路径的页面
      });
    }
  }
};
</script>

<style scoped>
/* 样式代码保持不变 */
.container {
  width: 100%;
  height: 100vh;
  background-image: url('/static/background.jpg');
  background-size: cover;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.logo {
  margin-bottom: 40px;
}

.logo-image {
  width: 500px;
  height: 150px;
}

.form {
  margin-right: 30px;
  width: 80%;
}

/* 输入框和小眼睛图标的容器 */
.input-wrapper {
  position: relative;
  width: 100%;
}

.input {
  width: 100%;
  height: 45px;
  margin-bottom: 20px;
  padding: 0 15px;
  padding-right: 20px; /* 给小眼睛图标留出空间 */
  border-radius: 8px;
  border: none;
  background-color: rgba(255, 255, 255, 0.9);
}

/* 小眼睛图标 */
.eye-icon {
  position: absolute;
  top: 50%;
  right: 10px; /* 调整右侧位置 */
  transform: translateY(-50%);
  font-size: 24px;
  cursor: pointer;
}

.forgot-password {
  color: white;
  text-align: right;
  margin-bottom: 20px;
}

.login-btn, .register-btn {
  width: 100%;
  height: 45px;
  margin-bottom: 15px;
  border-radius: 25px;
  background-color: #00bcd4;
  color: white;
  font-size: 16px;
  border: none;
  cursor: pointer;
  margin-left: 12px;
}

.register-btn {
  background-color: #00838f;
}

.agreement {
  display: flex;
  align-items: center;
  margin-top: 20px;
}

.checkbox {
  width: 20px;
  height: 20px;
  margin-right: 10px;
}

.label-text {
  font-size: 14px;
  color: white;
}
</style>
