<template>
  <view class="pulish-container">
    <!-- 返回按钮 -->
    <view class="back-button" @click="goBack">
      <image src="/static/back.png" class="back-icon" />
    </view>
    <!-- 发布项目页面内容 -->
    <view class="content">
      <view class="title">发布项目</view>
      
      <!-- 表单部分 -->
      <view class="form">
        <view class="form-item">
          <text class="label">项目名称</text>
          <input class="input" v-model="projectName" placeholder="请输入" />
        </view>
        <view class="form-item">
          <text class="label">项目组别</text>
          <input class="input" v-model="projectCategory" placeholder="请输入" />
        </view>
        <view class="form-item">
          <text class="label">人数需求</text>
          <input class="input" v-model="peopleNeeded" placeholder="请输入" />
        </view>
        <view class="form-item">
          <text class="label">公司状况</text>
          <input class="input" v-model="companyStatus" placeholder="请输入" />
        </view>
        <view class="form-item">
          <text class="label">项目描述</text>
          <textarea class="input" v-model="projectDescription" placeholder="请输入" />
        </view>
        <view class="form-item">
          <text class="label">图片</text>
          <view class="upload-area" @click="uploadImage">
            <image v-if="imageUrl" :src="imageUrl" class="uploaded-image" />
            <text v-else class="upload-placeholder">点击上传图片</text>
          </view>
        </view>
        <button class="submit-button" @click="submitProject">确认</button>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      projectName: '',
      projectCategory: '',
      peopleNeeded: '',
      companyStatus: '',
      projectDescription: '',
      imageUrl: '',
    };
  },
  onShow() {
    this.refreshPage();
  },
  methods: {
    goBack() {
      uni.switchTab({
        url: '/pages/tabbar/mine/mine'
      });
    },
    refreshPage() {
      this.loadProjects();
      this.calculateListHeight();
      this.updateCurrentTime(); // 更新当前时间
    },
    loadProjects() {
      const projects = uni.getStorageSync('projects') || [];
      console.log('当前项目列表:', projects);
    },
    calculateListHeight() {
      console.log('计算列表高度...');
    },
    updateCurrentTime() {
      console.log('当前时间:', new Date().toLocaleString());
    },
    uploadImage() {
      uni.chooseImage({
        count: 1,
        success: (res) => {
          this.imageUrl = res.tempFilePaths[0];
        }
      });
    },
    submitProject() {
      // 发送 POST 请求到服务器
      uni.request({
        url: 'http://ci86ph16222.vicp.fun/addProject/', // 使用您的服务器地址
        method: 'POST',
        header: {
          'Content-Type': 'application/x-www-form-urlencoded' // 设置请求头为表单编码
        },
        data: {
          projectname: this.projectName,
          projectteam: this.projectCategory,
          projectpeople: this.peopleNeeded,
          companysituation: this.companyStatus,
          projectdescription: this.projectDescription
        },
        success: (res) => {
          console.log(res); // 打印服务器返回的完整响应

          if (res.statusCode === 200 && res.data.status === 'success') {
            uni.showToast({
              title: '项目发布成功',
              icon: 'success'
            });

            // 跳转到我的项目页面
            uni.navigateTo({
              url: '/pages/myproject/myproject'
            });
          } else {
            uni.showToast({
              title: res.data.message || '项目发布失败',
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
    }
  }
};
</script>

<style>
.pulish-container {
  width: 100%;
  height: 100vh;
  background-color: #012C54;
  position: relative;
  padding: 20px;
}

.back-button {
  position: absolute;
  top: 20px;
  left: 10px;
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.back-icon {
  width: 24px;
  height: 24px;
}

.title {
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #ffffff;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.form-item {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.label {
  width: 80px;
  color: #ffffff;
}

.input {
  flex: 1;
  height: 40px;
  border-radius: 5px;
  padding: 0 10px;
  background-color: #ffffff;
  margin-right: 30px; /* 调整输入框与右侧边界的距离 */
}

.upload-area {
  width: calc(100%); /* 减去两边的间距 */
  margin-right: 30px; /* 确保与右侧有间距 */
  padding-top: 50%; /* 16:9 的比例 */
  background-color: #eee;
  border-radius: 5px;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  overflow: hidden;
}

.uploaded-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.upload-placeholder {
  color: #999;
  font-size: 14px;
}

.submit-button {
  width: 80%;
  height: 40px;
  background-color: #00C1DE;
  border: none;
  border-radius: 5px;
  color: #ffffff;
  font-size: 16px;
  margin-top: 20px;
  margin-right: 50px;
}
</style>
