const sectionsCount = $("section").length;
let activeIndex = 0;

// 监听用户按下空格和方向键的事件
$(document).on("keydown", (e) => {
  e.preventDefault();
  if (e.key === " " || e.key === "ArrowRight") {
    goRight();
  }
  if (e.key === "ArrowLeft") {
    goLeft();
  }
});

// 监听按钮点击事件
$(".btn.left").click(goLeft);
$(".btn.right").click(goRight);


// 切换下一张的函数
function goLeft() {
  if (activeIndex === 0) {
    return;
  }
  if (activeIndex == 1) {
      document.getElementById("left").disabled = true
      // console.log(document.getElementById("left").style.display.value)
      document.getElementById("left").style.display = 'none'
  }
  activeIndex -= 1;
  switchPage(activeIndex);
  document.getElementById("page").innerHTML = activeIndex + 1  + ' / ' + 5
  // inner = document.getElementById("page").innerHTML
  // console.log(inner)
}


if (activeIndex > 0) {
  document.getElementById("left").disabled = false
  console.log(document.getElementById("left").style.display)
  // document.getElementById("left").style.display = false
  document.getElementById("left").style.display = 'block'

}
if (activeIndex == 4) {
  document.getElementById("right").disabled = true
  document.getElementById("right").display = 'none'
  console.log(document.getElementById("right"))
  // console.log(document.getElementById("right"))
}


// 切换上一张的函数
function goRight() {
  if (activeIndex === sectionsCount - 1) {
    // document.getElementById("right").disabled = true
    document.getElementById("right").display = 'none'
    return;
  }
  document.getElementById("left").disabled = ""
  activeIndex += 1;
  // if (activeIndex >= 4) {
  //   document.getElementById("right").disabled = true
  //   console.log(document.getElementById("right"))
  // }
  switchPage(activeIndex);
  // inner = document.getElementById("page").innerHTML.split(" ")[0]
  document.getElementById("page").innerHTML = activeIndex + 1 + ' / ' + 5

}

function switchPage(activeIndex) {
  document.getElementById("left").style.display = 'block'
  document.getElementById("right").disabled = false
  document.getElementById("right").style.display = 'block'
  if (activeIndex == 0) {
    document.getElementById("left").disabled = true
    // console.log(document.getElementById("left").style.display.value)
    document.getElementById("left").style.display = 'none'
}
if (activeIndex == 4) {
  document.getElementById("right").disabled = true
  document.getElementById("right").style.display = 'none'
  console.log(document.getElementById("right"))
  // console.log(document.getElementById("right"))
}

  // TODO: 请补充该函数，实现根据activeIndex切换页面的功能，并且在到达最后一页或第一页时给相应的按钮添加disable类
  console.log(activeIndex)
  Array.from(document.querySelectorAll('section')).forEach(e => e.style.display = 'none');
  chosen = document.querySelectorAll('section')[activeIndex]
  chosen.style.display = 'block'

}
