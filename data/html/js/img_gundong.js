var banners = ["img/x1.jpg","img/x2.jpg","img/x3.jpg","img/x4.jpg","img/x5.jpg"]; // 图片地址
	var counter = 0;
		function run(){
			setInterval(cycle,1500);  //重复运行cycle函数，周期1000ms
		}
		function cycle(){
			counter++;
			if(counter == banners.length)	
				counter = 0;
			document.getElementById("banner").src = banners[counter];
		}
		