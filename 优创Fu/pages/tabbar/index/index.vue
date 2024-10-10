<template>
  <view class="container">
    <!-- 顶部部分，包括头像和用户名 -->
    <view class="header">
      <image src="/static/avatar.png" class="avatar" @click="goToMyPage"></image> <!-- 添加点击事件 -->
      <text class="username">Cypher</text>
    </view>

    <!-- 搜索框 -->
    <view class="search-bar">
      <input type="text" placeholder="搜索" v-model="searchQuery" @input="filterProjects" class="search-input" />
    </view>

    <!-- 推荐部分 -->
    <view class="recommend-section">
      <text class="recommend-title">项目推荐</text>

      <!-- 推荐列表 -->
      <scroll-view class="recommend-list" scroll-y="true">
        <view class="item" v-for="(project, index) in filteredProjects" :key="index">
          <view class="item-content">
            <!-- 图片部分 -->
            <image :src="project.image" class="project-image"></image>
            <!-- 文字介绍部分 -->
            <view class="project-info">
              <text class="project-title">{{ project.title }}</text>
              <text class="project-description">{{ project.description }}</text>
            </view>
          </view>
        </view>
      </scroll-view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '', // 搜索框输入的查询内容
      projects: [
        {
          title: '智控先锋',
          description: '研究生创意组, 已创建公司',
          image: '/static/proc1.png'
        },
        {
          title: '智控先锋',
          description: '研究生创业组, 已创建公司',
          image: '/static/2.jpg'
        },
        {
          title: '智慧先锋',
          description: '本科生创意, 未创建公司',
          image: '/static/3.jpg'
        }
      ],
      filteredProjects: [] // 用于保存筛选后的项目列表
    };
  },
  created() {
    // 初次加载时显示所有项目
    this.filteredProjects = this.projects;
  },
  onShow() {
    // 页面每次显示时刷新数据
    this.refreshPage();
  },
  methods: {
    refreshPage() {
      console.log("页面已刷新");
      this.filteredProjects = this.projects; // 简单刷新项目列表
      this.searchQuery = ''; // 清空搜索框内容
    },
    filterProjects() {
      // 根据搜索框输入的内容过滤项目
      const query = this.searchQuery.toLowerCase();
      this.filteredProjects = this.projects.filter((project) => {
        return (
          project.title.toLowerCase().includes(query) ||
          project.description.toLowerCase().includes(query)
        );
      });
    },
    // 跳转到 mypage 页面
    goToMyPage() {
      uni.navigateTo({
        url: '/pages/mypage/mypage' // 假设你的 mypage 页面路径是 /pages/mypage/mypage
      });
    }
  }
};
</script>

<style scoped>
/* 整体容器样式 */
.container {
  width: 100vw;
  height: 100vh;
  background-color: #1c3b57;
  padding: 5vw;
  overflow: hidden;
}

/* 顶部头像和用户名部分 */
.header {
  display: flex;
  align-items: center;
  margin-bottom: 3vh;
  margin-right: 16vh;
}

.avatar {
  width: 15vw;
  height: 15vw;
  border-radius: 50%;
  margin-right: 3vw;
  cursor: pointer; /* 添加手形指针，表示头像可点击 */
}

.username {
  color: white;
  justify-content: center;
  font-size: 8vw;
  font-weight: bold;
  margin-left: 60px;
}

/* 搜索框样式 */
.search-bar {
  display: flex;
  justify-content: center;
  margin-bottom: 4vh;
}

.search-input {
  width: 90vw;
  height: 8vh;
  padding-left: 3vw;
  border-radius: 25px;
  background-color: white;
  border: none;
  font-size: 4vw;
}

/* 推荐部分样式 */
.recommend-section {
  width: 100%;
  flex-grow: 1;
}

.recommend-title {
  color: white;
  display: block;
  font-size: 6vw;
  font-weight: bold;
  margin-bottom: 40px;
}

/* 推荐列表样式 */
.recommend-list {
  display: flex;
  flex-direction: column;
  gap: 30px;
  align-items: center;
  height: 70vh;
  overflow-y: scroll;
}

/* 项目卡片样式 */
.item {
  background-color: #55ffff;
  border-radius: 10px;
  padding: 0;
  margin-bottom: 30px;
  width: 90%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #55ffff;
  overflow: hidden;
}

.item:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

/* 图片样式 */
.project-image {
  width: 100%;
  height: 180px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

/* 文字介绍部分 */
.project-info {
  padding: 15px;
  background-color: #ffffff;
}

.project-title {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 8px;
  letter-spacing: 1px;
  font-size: 20px;
}

.project-description {
  font-size: 14px;
  color: #666;
  margin-left: 30px;
  letter-spacing: 1px;
  font-size: 15px;
}
</style>
