<script setup>
import LogoCard from "@/components/LogoCard.vue";
import { onMounted, ref } from "vue";

const gh = () => {
    window.open("https://github.com/PCL-Community/PCL-GitView", "_blank");
};

onMounted(async () => {
    try {
        const labelList = await fetchLabel();
        if (labelList.length > 0) {
            localStorage.setItem("X-PG-Labels", JSON.stringify(labelList));
        }
    } catch (error) {
        console.error("获取标签失败：", error);
    }
});

const btnColor = ref(null)
const matchTheme = (e) => {
    if (e.matches) {
        btnColor.value = "#0665D2"
    } else {
        btnColor.value = "#0c72e7"
    }
};
window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", matchTheme);
matchTheme(window.matchMedia("(prefers-color-scheme: dark)"));
</script>

<template>
    <div class="home-view">
        <div class="left">
            <span class="title">PCL GitView</span>
            <br />
            <span class="subtitle"> 基于 Vue 和 GitHub Rest API 全新构建 </span>
            <br /><br />
            <span>
                <el-button type="primary" :color="btnColor" @click="$router.push('/Intro')">
                    什么是 PCL GitView ?
                </el-button>
                <el-button type="info" @click="$router.push('/IssuesOverview')">
                    快速开始
                </el-button>
                <el-button type="info" @click="gh()">GitHub</el-button>
            </span>
        </div>
        <div class="right">
            <logo-card class="main-logo" />
        </div>
    </div>
</template>

<style scoped lang="less">
div.home-view {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 60px;
    div.left {
        width: 50%;
        padding-left: 48px;
        span.title {
            font-size: 3rem;
            font-weight: 550;
            background: linear-gradient(
                to bottom right,
                #1381ff 0%,
                #0059bf 80%
            );
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
        }
        span.subtitle {
            font-size: 2.5rem;
            font-weight: 550;
        }
        .el-button {
            padding: 18px 24px;
            height: 36px;
        }
    }
    div.right {
        width: 50%;
    }
}

.main-logo {
    scale: 0.5;
    transition: scale 0.3s ease-in-out;
    &:hover {
        scale: 0.55;
    }
}
</style>
