window.onload = function () {
    var DaisyMember = ["吳婉淩", "李孟純", "李采潔", "林潔心", "林佳霓", "冼迪琦", "柏 靈", "宮田留佳", "陳詩雅", "國興瑀", "董子瑄", "賈宜蓁", "蔡亞恩", "潘姿怡"]
    var BellflowerMember = ["王逸嘉", "李佳俐", "邱品涵", "周家安", "林 倢", "翁彤薰", "高云珏", "張法法", "蔡伊柔", "鄭妤葳", "劉語晴", "劉潔明", "藤井麻由", "羅瑞婷"]
    var SakuraMember = ["小山美玲", "本田柚萱", "吳騏卉", "周佳郁", "林易沄", "林家瑩", "林于馨", "林亭莉", "袁子筑", "高硯晨", "張羽翎", "曾詩羽", "鄭佳郁", "劉曉晴"]
    let list = ""
    DaisyMember.forEach(element => {
        list += `<option>${element}</option>`
    });
    $("#chooseMember").html(list)
    $("#chooseTeam").change(function () {
        if ($("#chooseTeam").val() == "Daisy") {
            let list = ""
            DaisyMember.forEach(element => {
                list += `<option>${element}</option>`
            });
            $("#chooseMember").html(list)
        }
        if ($("#chooseTeam").val() == "Bellflower") {
            let list = ""
            BellflowerMember.forEach(element => {
                list += `<option>${element}</option>`
            });
            $("#chooseMember").html(list)
        }
        if ($("#chooseTeam").val() == "Sakura") {
            let list = ""
            SakuraMember.forEach(element => {
                list += `<option>${element}</option>`
            });
            $("#chooseMember").html(list)
        }
    })
}

function getvalue() {
    var time = document.getElementById("date")
    var name = document.getElementById("chooseMember")
    pushvalue(time.value, name.value)
}

function pushvalue(time, name) {
    arr.push([time, name])
}

function showtext123(text) {
    // document.getElementById("showtext").style.display = "inline"
    // document.getElementById("showtext").innerHTML = text
    alert(text);
}

function start() {
    alert(window.arr)
}
var arr = []