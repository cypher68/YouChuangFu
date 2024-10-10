<template>
  <view class="myproject-container">
    <!-- 返回按钮 -->
    <view class="back-button" @click="goBack">
      <image src="/static/back.png" class="back-icon" />
    </view>
    
    <view class="title">我的项目</view>

    <!-- 项目列表部分，可以滚动 -->
    <scroll-view class="project-list" scroll-y="true" :style="{ height: listHeight + 'px' }">
      <view v-if="projects.length > 0">
        <view v-for="(project, index) in projects" :key="index" class="project-item">
          <view class="item-content">
            <!-- 项目信息部分 -->
            <view class="project-header">
              <text class="project-name">{{ project.name }}</text>
              <text class="project-status">招募中</text>
            </view>
            <view class="project-details">
              <text class="createdTime">🕒 创建时间: {{ project.createdTime }}</text>
              <text class="category">👥 项目组别: {{ project.category }}</text>
            </view>
            <view class="actions">
              <view class="wait-icon">➕ 待招</view>
              <button class="delete-button" @click="deleteProject(index)">删除</button>
            </view>
          </view>
        </view>
      </view>
      <view v-else class="no-projects">暂无项目</view>
    </scroll-view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      projects: [],
      listHeight: 0,
    };
  },
  onShow() {
    this.loadProjects(); // 从服务器加载项目
    this.calculateListHeight();
  },
  methods: {
    goBack() {
      uni.switchTab({
        url: '/pages/tabbar/mine/mine'
      });
    },
    loadProjects() {
      // 发送请求从服务器获取项目数据
      uni.request({
        url: 'http://ci86ph16222.vicp.fun/addProject/', // 替换为您的获取项目的 API URL
        method: 'GET',
        success: (res) => {
          if (res.statusCode === 200 && res.data) {
            this.projects = res.data.projects || []; // 假设返回的数据结构中包含项目数组
            console.log('从服务器获取到的项目:', this.projects);
          } else {
            uni.showToast({
              title: '加载项目失败',
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
    calculateListHeight() {
      const systemInfo = uni.getSystemInfoSync();
      const fixedHeight = 130; // 固定顶部的高度
      this.listHeight = systemInfo.windowHeight - fixedHeight;
    },
    deleteProject(index) {
      this.projects.splice(index, 1);
      uni.setStorageSync('projects', this.projects);
      this.loadProjects();
    },
  },
};
</script>

<style>
.myproject-container {
  padding: 20px;
  background-color: #012C54;
  min-height: 100vh;
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
  z-index: 10;
}

.back-icon {
  width: 24px;
  height: 24px;
}

.title {
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  color: #ffffff;
  margin-bottom: 10px;
  margin-top: 20px; /* 为了避免被返回按钮遮挡 */
}

.project-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding-top: 20px;
}

.project-item {
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  padding: 15px;
  margin-bottom: 10px;
}

.item-content {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.project-name {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.project-status {
  font-size: 12px;
  color: #d32f2f;
  border: 1px solid #d32f2f;
  border-radius: 4px;
  padding: 2px 5px;
}

.project-details {
  display: flex;
  flex-direction: column;
  gap: 5px;
  font-size: 14px;
  color: #666;
}

.actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.wait-icon {
  font-size: 14px;
  color: #555;
}

.delete-button {
  background-color: #ff4d4f;
  color: #ffffff;
  border: none;
  border-radius: 100px;
  padding: 0px 30px;
  cursor: pointer;
  align-self: flex-end;
}

.no-projects {
  text-align: center;
  color: #ffffff;
  font-size: 16px;
}
</style>
