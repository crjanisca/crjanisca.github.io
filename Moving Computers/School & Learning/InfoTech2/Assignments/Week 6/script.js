let gameData = {
    money: 0,
    moneyPerClick: 0.25,
    guitars: 0,
    skill: 0,
    lessonPrice: 10,
    guitarPrice: 500,
    bandMembers: 1,
    stage: 0,
    guitarStatus: 0,
    hirePrice: 1000,
    marketing: 0,
    adPrice: 2000,
    managementPrice: 10000,
    streamPrice: 25000,
    radioPrice: 50000,
    signDeal: 100000
}

function earnMoney() {
    gameData.money += gameData.moneyPerClick;
    localStorage.setItem("clickCounter", JSON.stringify(gameData));
    let roundMoney = parseFloat(gameData.money);
    let moneyOwned = roundMoney.toFixed(2);
    document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
}

function takeLesson() {
    if (gameData.money >= gameData.lessonPrice) {
        gameData.money -= gameData.lessonPrice;
        gameData.skill += 1
        let roundMoney = parseFloat(gameData.money);
        let moneyOwned = roundMoney.toFixed(2);
        document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
        document.getElementById("skillLevel").innerHTML = "Skill Level: " + gameData.skill;
        if (gameData.skill == 5) {
            gameData.moneyPerClick = 1;
            gameData.lessonPrice = 30;
            gameData.stage = 1;
            document.getElementById("gameStage").innerHTML = "Stage 1: Beginner";
            document.getElementById("lessonTaking").innerHTML = "Take Lesson ($" + gameData.lessonPrice + ")";
            document.getElementById("moneyEarned").innerHTML = "Earn Money (+$" + gameData.moneyPerClick + ")";
        }
        if (gameData.skill == 10) {
            gameData.moneyPerClick = 10;
            gameData.lessonPrice = 100;
            document.getElementById("lessonTaking").innerHTML = "Take Lesson ($" + gameData.lessonPrice + ")";
            document.getElementById("moneyEarned").innerHTML = "Earn Money (+$" + gameData.moneyPerClick + ")";
        
        }
        if (gameData.skill == 20) {
            gameData.moneyPerClick = 30;
            document.getElementById("moneyEarned").innerHTML = "Earn Money (+$" + gameData.moneyPerClick + ")";
            const deleteButton = document.getElementById("lessonTaking");
            const parent = deleteButton.parentNode;
            parent.removeChild(deleteButton);
        }
    }
}

function buyGuitar() {
    if (gameData.money >= gameData.guitarPrice) {
        gameData.money -= gameData.guitarPrice;
        let roundMoney = parseFloat(gameData.money);
        let moneyOwned = roundMoney.toFixed(2);
        document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
        document.getElementById("guitarStatus").innerHTML = "Guitar Status: New";
        gameData.guitarStatus = 1;
        const deleteButton = document.getElementById("buyNewGuitar");
        const parent = deleteButton.parentNode;
        parent.removeChild(deleteButton);
        const deleteButton2 = document.getElementById("breakNewGuitar");
        const parent2 = deleteButton2.parentNode;
        parent2.removeChild(deleteButton2);
        document.getElementById('hire-band-members').style.visibility = 'visible';
    }
}

function hireDrummer() {
    if (gameData.money >= gameData.hirePrice) {
        gameData.money -= gameData.hirePrice;
        gameData.bandMembers += 1
        let roundMoney = parseFloat(gameData.money);
        let moneyOwned = roundMoney.toFixed(2);
        document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
        document.getElementById("bandMembers").innerHTML = "Band Members: " + gameData.bandMembers + "/4";
        const deleteButton = document.getElementById("hireDrummer");
        const parent = deleteButton.parentNode;
        parent.removeChild(deleteButton);
    }
}

function hireBassist() {
    if (gameData.money >= gameData.hirePrice) {
        gameData.money -= gameData.hirePrice;
        gameData.bandMembers += 1
        let roundMoney = parseFloat(gameData.money);
        let moneyOwned = roundMoney.toFixed(2);
        document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
        document.getElementById("bandMembers").innerHTML = "Band Members: " + gameData.bandMembers + "/4";
        const deleteButton = document.getElementById("hireBassist");
        const parent = deleteButton.parentNode;
        parent.removeChild(deleteButton);
    }
}

function hireVocalist() {
    if (gameData.money >= gameData.hirePrice) {
        gameData.money -= gameData.hirePrice;
        gameData.bandMembers += 1
        let roundMoney = parseFloat(gameData.money);
        let moneyOwned = roundMoney.toFixed(2);
        document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
        document.getElementById("bandMembers").innerHTML = "Band Members: " + gameData.bandMembers + "/4";
        const deleteButton = document.getElementById("hireVocalist");
        const parent = deleteButton.parentNode;
        parent.removeChild(deleteButton);
    }
}

function checkStage() {
    if (gameData.stage == 1) {
        if (gameData.skill == 20 && gameData.guitarStatus == 1 && gameData.bandMembers == 4) {
            document.getElementById("gameStage").innerHTML = "Stage 2: Local Fame";
            gameData.stage = 2;
            document.getElementById('marketing').style.visibility = 'visible';
        }
        setTimeout(checkStage, 0);
    }
}

setInterval(checkStage, 1000)

setTimeout(() => {
    gameData.stage = 1;
}, 1500);

setInterval(function() {
    gameData.money += gameData.marketing;
    let roundMoney = parseFloat(gameData.money);
    let moneyOwned = roundMoney.toFixed(2);
    document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
}, 1000);

function buyAds() {
    if (gameData.money >= gameData.adPrice) {
        gameData.money -= gameData.adPrice;
        gameData.marketing += 10;
        let roundMoney = parseFloat(gameData.money);
        let moneyOwned = roundMoney.toFixed(2);
        document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
        const deleteButton = document.getElementById("buyAds");
        const parent = deleteButton.parentNode;
        parent.removeChild(deleteButton);
    }
}

function hireMarketingTeam() {
    if (gameData.money >= gameData.managementPrice) {
        gameData.money -= gameData.managementPrice;
        gameData.marketing += 50;
        gameData.moneyPerClick = gameData.moneyPerClick * 2;
        let roundMoney = parseFloat(gameData.money);
        let moneyOwned = roundMoney.toFixed(2);
        document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
        document.getElementById("moneyEarned").innerHTML = "Earn Money (+$" + gameData.moneyPerClick + ")";
        const deleteButton = document.getElementById("hireMarketingTeam");
        const parent = deleteButton.parentNode;
        parent.removeChild(deleteButton);
    }
}

function checkMarketing() {
    if (gameData.marketing >= 60) {
        document.getElementById('distribution').style.visibility = 'visible';
    setTimeout(checkMarketing, 0);
    }
}

setInterval(checkMarketing, 1000)

setTimeout(() => {
    gameData.marketing >= 60;
}, 1500);



function streamMusic() {
    if (gameData.money >= gameData.streamPrice) {
        gameData.money -= gameData.streamPrice;
        gameData.marketing += 40;
        gameData.moneyPerClick = gameData.moneyPerClick * 2;
        let roundMoney = parseFloat(gameData.money);
        let moneyOwned = roundMoney.toFixed(2);
        document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
        document.getElementById("moneyEarned").innerHTML = "Earn Money (+$" + gameData.moneyPerClick + ")";
        const deleteButton = document.getElementById("streamMusic");
        const parent = deleteButton.parentNode;
        parent.removeChild(deleteButton);
    }
}

function musicOnRadio() {
    if (gameData.money >= gameData.radioPrice) {
        gameData.money -= gameData.radioPrice;
        gameData.moneyPerClick = gameData.moneyPerClick * 4;
        let roundMoney = parseFloat(gameData.money);
        let moneyOwned = roundMoney.toFixed(2);
        document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
        document.getElementById("moneyEarned").innerHTML = "Earn Money (+$" + gameData.moneyPerClick + ")";
        const deleteButton = document.getElementById("musicOnRadio");
        const parent = deleteButton.parentNode;
        parent.removeChild(deleteButton);
    }
}

function signDeal() {
    if (gameData.money >= gameData.signDeal) {
        gameData.money -= gameData.signDeal;
        gameData.marketing += 400;
        let roundMoney = parseFloat(gameData.money);
        let moneyOwned = roundMoney.toFixed(2);
        document.getElementById("totalMoney").innerHTML = "Bank Account: $" + moneyOwned;
        const deleteButton = document.getElementById("signDeal");
        const parent = deleteButton.parentNode;
        parent.removeChild(deleteButton);
        document.getElementById('toBeContinued').style.visibility = 'visible';
        document.getElementById("gameStage").innerHTML = "Stage 3: To Be Continued...";
        gameData.stage = 3
    }
}