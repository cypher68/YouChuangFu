<template>
  <view class="container">
    <!-- Logo 和标题 -->
    <view class="title">
      <text>注册</text>
    </view>

    <!-- 注册表单 -->
    <view class="form">
      <input v-model="username" type="text" placeholder="输入账号" class="input" />
      <input v-model="password" type="password" placeholder="输入密码" class="input" />
      <input v-model="confirmPassword" type="password" placeholder="确认密码" class="input" />
    </view>

    <!-- 注册按钮 -->
    <button class="register-btn" @click="register">完成注册</button>

    <!-- 用户协议 -->
    <view class="agreement">
      <input type="checkbox" id="agreement" v-model="agreed" class="checkbox" />
      <label for="agreement" class="label-text">
        登录/注册表示您同意《用户协议》和《隐私政策》</label>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      username: '', // 输入的用户名
      password: '', // 输入的密码
      confirmPassword: '', // 确认密码
      agreed: false, // 是否同意用户协议
    };
  },
  methods: {
    // 注册逻辑
    register() {
      if (!this.agreed) {
        uni.showToast({
          title: '请同意用户协议',
          icon: 'none'
        });
        return;
      }

      if (this.password !== this.confirmPassword) {
        uni.showToast({
          title: '密码和确认密码不一致',
          icon: 'none'
        });
        return;
      }

      const username = this.username.trim();
      const password = this.password;

      if (!username) {
        uni.showToast({
          title: '用户名不能为空',
          icon: 'none'
        });
        return;
      }

      // 日志输出
      console.log('用户名：', username);
      console.log('密码：', password);

      // URL 编码的数据
      const data = `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`;

      // 发起注册请求到服务器
      uni.request({
        url: 'http://ci86ph16222.vicp.fun/addUser/',
        method: 'POST',
        header: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: data,
        success: (res) => {
          console.log('服务器响应：', res);
          if (res.data && res.data.status === 'success') {
            uni.showToast({
              title: '注册成功',
              icon: 'success'
            });
            // 跳转到登录页面
            setTimeout(() => {
              uni.navigateTo({
                url: '/pages/login/login'
              });
            }, 2000);
          } else {
            uni.showToast({
              title: res.data.message || '注册失败，服务器返回错误',
              icon: 'none'
            });
          }
        },
        fail: (err) => {
          console.error('请求失败：', err);
          uni.showModal({
            title: '错误信息',
            content: `错误码：${err.errCode || '未知'}\n错误信息：${err.errMsg || '未知'}`,
            showCancel: false
          });
        }
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
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.title {
  font-size: 40px;
  font-weight: bold;
  margin-bottom: 40px;
  margin-left: -35px;
}

.form {
  width: 80%;
  max-width: 400px;
  margin-bottom: 30px;
  margin-right: 70px;
}

.input {
  width: 100%;
  height: 50px;
  margin-bottom: 20px;
  padding: 0 15px;
  border-radius: 8px;
  border: 1px solid #dcdcdc;
  background-color: #e8f0fe;
  font-size: 16px;
}

.register-btn {
  width: 90%;
  height: 50px;
  margin-bottom: 20px;
  margin-right: 70px;
  border-radius: 25px;
  background-color: #00bcd4;
  color: white;
  font-size: 18px;
  border: none;
  text-align: center;
  cursor: pointer;
  max-width: 400px;
}

.agreement {
  display: flex;
  align-items: center;
  width: 80%;
  max-width: 400px;
  justify-content: center;
}

.checkbox {
  width: 18px;
  height: 18px;
  margin-right: 20px;
}

.label-text {
  font-size: 11px;
  color: #555;
  margin-left: 0;
}
</style>
