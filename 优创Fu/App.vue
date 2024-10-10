<script>
	export default {
		onLaunch: function() {
		    console.log('App Launch');
		  },
		  onShow: function() {
		    console.log('App Show');
		    // 强制重新应用背景图片样式
		    document.body.style.backgroundImage = "url('/static/background.png')";
		    document.body.style.backgroundSize = "cover";
		    document.body.style.backgroundPosition = "center";
		    document.body.style.backgroundRepeat = "no-repeat";
		  },
		  onHide: function() {
		    console.log('App Hide');
		  }
	}
</script>

<style>
	/*每个页面公共css */
	body{
		background-image: url('/static/background.png');
		background-size: cover;
		background-position: center; 
		background-repeat: no-repeat;
	}
</style>
