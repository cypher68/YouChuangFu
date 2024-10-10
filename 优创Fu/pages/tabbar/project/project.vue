<template>
  <view class="project-container">
    <view class="fixed-top">
      <!-- 页面标题 -->
      <view class="title">所有项目</view>
      
      <!-- 分割线 -->
      <view class="divider"></view>
      
      <!-- 搜索框 -->
      <view class="search-bar">
        <input
          type="text"
          placeholder="搜索项目名称或组别"
          v-model="searchQuery"
          @input="filterProjects"
          class="search-input"
        />
      </view>
    </view>

    <!-- 项目列表部分，可以滚动 -->
    <scroll-view class="project-list" scroll-y="true" :style="{ height: listHeight + 'px' }">
      <view v-if="filteredProjects.length > 0">
        <view v-for="(project, index) in filteredProjects" :key="index" class="project-item">
          <view class="item-content">
            <!-- 项目信息部分 -->
            <view class="project-header">
              <text class="project-name">{{ project.projectname }}</text>
              <text class="project-status">招募中</text>
            </view>
            <view class="project-details">
              <text class="time">🕒 {{ project.created_at }}</text>
              <text class="category">👥 {{ project.projectteam }}</text>
            </view>
            <view class="actions">
              <view class="wait-icon">➕ 待招</view>
              <button class="join-button">立即加入</button>
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
      filteredProjects: [],
      searchQuery: '',
      listHeight: 0,
    };
  },
  onShow() {
    this.loadProjects();
    this.calculateListHeight();
  },
  methods: {
    loadProjects() {
      // 发起请求从后端获取项目数据
      uni.request({
        url: 'http://ci86ph16222.vicp.fun/listProjects/?sort_by=projectname', // 使用您的后端 API 地址
        method: 'GET',
        success: (res) => {
          console.log('API 响应:', res); // 打印完整的响应数据

          // 检查响应的状态码和数据类型
          if (res.statusCode === 200) {
            const data = res.data;
            if (data.projects && Array.isArray(data.projects)) {
              // 确保数据包含 projects 字段并且是一个数组
              this.$set(this, 'projects', data.projects);
              this.$set(this, 'filteredProjects', data.projects);
              console.log('项目数据:', this.projects); // 打印项目数据
            } else {
              // 数据格式不正确，显示错误
              console.error('返回的数据格式不正确:', data);
              uni.showToast({
                title: '数据格式错误，请检查后端返回的数据结构',
                icon: 'none'
              });
            }
          } else {
            // 非 200 状态码，显示错误信息
            console.error(`请求失败，状态码: ${res.statusCode}`, res.data);
            uni.showToast({
              title: `请求失败，状态码: ${res.statusCode}`,
              icon: 'none'
            });
          }
        },
        fail: (err) => {
          console.error('请求失败:', err);
          uni.showToast({
            title: '网络错误，请检查连接',
            icon: 'none'
          });
        }
      });
    },
    filterProjects() {
      const query = this.searchQuery.toLowerCase();
      this.filteredProjects = this.projects.filter((project) =>
        project.projectname.toLowerCase().includes(query) ||
        project.projectteam.toLowerCase().includes(query)
      );
    },
    calculateListHeight() {
      const systemInfo = uni.getSystemInfoSync();
      const fixedHeight = 180; // 固定顶部的高度（包括搜索栏和分割线）
      this.listHeight = systemInfo.windowHeight - fixedHeight;
    },
  },
};
</script>

<style scoped>
.project-container {
  padding: 20px;
  background-color: #012C54;
  min-height: 100vh;
}

.fixed-top {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: #012C54;
  z-index: 10;
  padding: 20px;
}

.title {
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  color: #ffffff;
  margin-bottom: 20px;
}

.divider {
  height: 2px;
  background-color: #ffffff;
  margin: 10px 0;
}

.search-bar {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.search-input {
  width: 90%;
  height: 40px;
  padding-left: 10px;
  border-radius: 20px;
  background-color: #ffffff;
  border: none;
  font-size: 14px;
}

.project-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding-top: 180px; /* 为了避免搜索框遮挡 */
}

.project-item {
  background-color: #ffffff;
  border-radius: 8px;
  overflow: hidden;
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
  gap: 10px;
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

.join-button {
  background-color: #d32f2f;
  color: #ffffff;
  border: none;
  border-radius: 100px;
  padding: 0px 10px;
  cursor: pointer;
}

.no-projects {
  text-align: center;
  color: #ffffff;
  font-size: 16px;
  margin-top: 20px;
}
</style>
