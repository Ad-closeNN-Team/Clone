<script setup>
import { reactive } from "vue";

const props = defineProps({
    issueId: String,
    issueStatus: String,
    issueTitle: String,
    labels: Array,
});

const issueData = reactive({
    isIssueOpen: props.issueStatus === "open",
    isIssueClosed: props.issueStatus === "closed",
    isLabeldBug: props.labels.includes("· Bug"),
    isLabeldFeat: props.labels.includes("· 优化"),
    isLabeldNew: props.labels.includes("· 新功能"),
    isLabeldCreated: props.labels.includes("新反馈"),
    isLabeldNeedReprod: props.labels.includes("需要社区复现"),
    isLabeldNeedHelp: props.labels.includes("需要社区帮助"),
    isLabeldInfix: props.labels.includes("处理中"),
    isLabeldFixed: props.labels.includes("完成"),
    isLabeldLevelP0: props.labels.includes("🟪 极高"),
    isLabeldLevelP1: props.labels.includes("🟥 高"),
    issueStatusIcon:
        props.issueStatus === "open"
            ? "open"
            : props.labels.includes("完成")
            ? "fixed"
            : "closed",
    theme: null,
    themeType: "light",
});

// Theme Change Detector
const matchTheme = (e) => {
    if (e.matches) {
        issueData.theme = "dark";
    } else {
        issueData.theme = "light";
    }
};
window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", matchTheme);
matchTheme(window.matchMedia("(prefers-color-scheme: dark)"));

const handleOpen = () => {
    window.open(`https://github.com/Hex-Dragon/PCL2/issues/${props.issueId}`);
};
</script>

<template>
    <el-card shadow="hover" @click="handleOpen()">
        <div class="content">
            <div class="icon">
                <el-icon
                    v-if="issueData.issueStatusIcon === 'open'"
                    :size="24"
                    color="var(--el-color-warning)">
                    <Warning />
                </el-icon>
                <el-icon
                    v-if="issueData.issueStatusIcon === 'fixed'"
                    :size="24"
                    color="var(--el-color-success)">
                    <CircleCheck />
                </el-icon>
                <el-icon
                    v-if="issueData.issueStatusIcon === 'closed'"
                    :size="24"
                    color="var(--el-color-danger)">
                    <CircleClose />
                </el-icon>
            </div>
            <div class="left">
                <div class="main">
                    <span class="title">{{ props.issueTitle }}</span>
                    <div class="labels">
                        <el-tag
                            v-if="issueData.isLabeldBug"
                            :effect="issueData.themeType"
                            type="danger">
                            · Bug
                        </el-tag>
                        <el-tag
                            v-if="issueData.isLabeldFeat"
                            :effect="issueData.themeType"
                            type="success">
                            · 优化
                        </el-tag>
                        <el-tag
                            v-if="issueData.isLabeldNew"
                            :effect="issueData.themeType"
                            type="primary">
                            · 新功能
                        </el-tag>
                        <el-tag
                            v-if="issueData.isLabeldCreated"
                            :effect="issueData.themeType"
                            class="customstyle"
                            color="#E93F00">
                            新反馈
                        </el-tag>
                        <el-tag
                            v-if="issueData.isLabeldNeedReprod"
                            :effect="issueData.themeType"
                            class="customstyle"
                            color="#E93F00">
                            需要社区复现
                        </el-tag>
                        <el-tag
                            v-if="issueData.isLabeldInfix"
                            :effect="issueData.themeType"
                            class="customstyle"
                            style="color: black"
                            color="#FBCA04">
                            处理中
                        </el-tag>
                        <el-tag
                            v-if="issueData.isLabeldFixed"
                            :effect="issueData.themeType"
                            class="customstyle"
                            color="#0E8A16">
                            完成
                        </el-tag>
                        <el-tag
                            v-if="issueData.isLabeldNeedHelp"
                            :effect="issueData.themeType"
                            class="customstyle"
                            color="#E93F00">
                            需要社区帮助
                        </el-tag>
                        <el-tag
                            v-if="issueData.isLabeldLevelP0"
                            :effect="issueData.themeType"
                            type="info">
                            🟪 极高
                        </el-tag>
                        <el-tag
                            v-if="issueData.isLabeldLevelP1"
                            :effect="issueData.themeType"
                            type="info">
                            🟥 高
                        </el-tag>
                    </div>
                </div>
                <sup>#{{ props.issueId }}</sup>
            </div>
        </div>
    </el-card>
</template>

<style scoped lang="less">
div.content {
    display: flex;
    justify-content: center;
    align-items: center;
    div.icon {
        transform: translateX(-25%);
        margin-right: 20px;
        .el-icon {
            margin-top: 4px;
        }
    }
    div.left {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 6px;
        div.main {
            display: flex;
            gap: 12px;
            align-items: center;
            span.title {
                max-width: 100px;
                text-overflow: ellipsis;
                white-space: nowrap;
                overflow: hidden;
            }
            div.labels{
                width: 182.29px;
            }
        }
        sup {
            color: var(--el-color-info);
            font-size: 12px;
        }
    }
}

div.labels {
    display: flex;
    gap: 8px;
}

.el-card {
    cursor: pointer;
    margin-right: 12px;
}

.el-tag.customstyle {
    border: none;
    color: white;
}
</style>
