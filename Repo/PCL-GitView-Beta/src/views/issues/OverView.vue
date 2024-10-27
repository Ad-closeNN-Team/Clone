<script setup>
import { onMounted, reactive, ref } from "vue";
import { applyAnimation } from "@/common/public";
import CustomLoading from "../../components/CustomLoading.vue";
import IssueCard from "@/components/IssueCard.vue";

const loadData = (data) => {
    const dataLabel = data[0],
        dataStatus = data[1],
        dataVaild = data[2];
    issueData.issueNewList = data[3];
    issueData.issueHighLevelList = data[4];
    issueData.issueNeedHelpList = data[5];
    const issueBug = dataLabel["· Bug"];
    issueTypeBug.value = issueBug;
    const issueFeat = dataLabel["· 优化"];
    issueTypeFeat.value = issueFeat;
    const issueNew = dataLabel["· 新功能"];
    issueTypeNew.value = issueNew;
    const issueOpen = dataStatus["◼️open"];
    issueTypeOpen.value = issueOpen;
    const issueClosed = dataStatus["◼️closed"];
    issueTypeClosed.value = issueClosed;
    const issueTotal = issueOpen + issueClosed;
    issueTypeTotal.value = issueTotal;
    const issueVaild = dataVaild["◼️valid"];
    issueTypeVaild.value = issueVaild;
    const issueInvaild = dataVaild["◼️invalid"];
    issueTypeInvaild.value = issueInvaild;
};

const issueData = reactive({
    data: null,
    issueNewList: [],
    issueHighLevelList: [],
    issueNeedHelpList: [],
    isLoadingFinish: false,
});
const issueTypeBug = ref(0);
const issueTypeBugT = applyAnimation(issueTypeBug);
const issueTypeFeat = ref(0);
const issueTypeFeatT = applyAnimation(issueTypeFeat);
const issueTypeNew = ref(0);
const issueTypeNewT = applyAnimation(issueTypeNew);
const issueTypeTotal = ref(0);
const issueTypeTotalT = applyAnimation(issueTypeTotal);
const issueTypeOpen = ref(0);
const issueTypeOpenT = applyAnimation(issueTypeOpen);
const issueTypeClosed = ref(0);
const issueTypeClosedT = applyAnimation(issueTypeClosed);
const issueTypeVaild = ref(0);
const issueTypeVaildT = applyAnimation(issueTypeVaild);
const issueTypeInvaild = ref(0);
const issueTypeInvaildT = applyAnimation(issueTypeInvaild);

// Loading Data
onMounted(() => {
    if (
        localStorage.getItem("X-Data") === "[]" ||
        localStorage.getItem("X-Data") === undefined ||
        localStorage.getItem("X-Data") === null
    ) {
        fetch("http://154.7.177.68:3101/getIssueList").then(async (res) => {
            const data = await res.json();
            localStorage.setItem("X-Data", JSON.stringify(data));
            loadData(data);
            issueData.data = data;
            issueData.isLoadingFinish = true;
        });
    } else {
        const data = JSON.parse(localStorage.getItem("X-Data"));
        loadData(data);
        issueData.data = data;
        issueData.isLoadingFinish = true;
    }
    console.log(issueData);
});
</script>

<template>
    <div class="OverView">
        <div class="data" v-if="issueData.isLoadingFinish">
            <el-card shadow="hover">
                <el-row
                    style="height: 120px; display: flex; align-items: center">
                    <el-col :span="8">
                        <el-statistic :value="`/`">
                            <template #title>
                                <span style="color: #e5b456">总计</span> /
                                <span style="color: #48bc91">开启</span> /
                                <span style="color: #cd5c64">关闭</span>
                            </template>
                            <template #prefix>
                                <span style="color: #e5b456">
                                    {{ Number.parseInt(issueTypeTotalT) }}
                                </span>
                                /
                                <span style="color: #48bc91">
                                    {{ Number.parseInt(issueTypeOpenT) }}
                                </span>
                            </template>
                            <template #suffix>
                                <span style="color: #cd5c64">
                                    {{ Number.parseInt(issueTypeClosedT) }}
                                </span>
                            </template>
                        </el-statistic>
                    </el-col>
                    <el-col :span="8">
                        <el-statistic :value="`/`">
                            <template #title>
                                <span style="color: #43a047">有效</span> /
                                <span style="color: #ed407a">无效</span>
                            </template>
                            <template #prefix>
                                <span style="color: #43a047">
                                    {{ Number.parseInt(issueTypeVaildT) }}
                                </span>
                            </template>
                            <template #suffix>
                                <span style="color: #ed407a">
                                    {{ Number.parseInt(issueTypeInvaildT) }}
                                </span>
                            </template>
                        </el-statistic>
                    </el-col>
                    <el-col :span="8">
                        <el-statistic :value="`/`">
                            <template #title>
                                <span style="color: #ff7043">Bug</span> /
                                <span style="color: #42a5f5">优化</span> /
                                <span style="color: #ab47bc">新功能</span>
                            </template>
                            <template #prefix>
                                <span style="color: #ff7043">
                                    {{ Number.parseInt(issueTypeBugT) }}
                                </span>
                                /
                                <span style="color: #42a5f5">
                                    {{ Number.parseInt(issueTypeFeatT) }}
                                </span>
                            </template>
                            <template #suffix>
                                <span style="color: #ab47bc">
                                    {{ Number.parseInt(issueTypeNewT) }}
                                </span>
                            </template>
                        </el-statistic>
                    </el-col>
                </el-row>
            </el-card>
            <el-row
                :gutter="20"
                style="
                    height: calc(100% - 20px - 20px - 120px - 20px);
                    margin-top: 20px;
                ">
                <el-col :span="8">
                    <el-card class="issueDisplayCard">
                        <template #header>
                            <div class="card-header">
                                <span>新反馈列表</span>
                            </div>
                        </template>
                        <div class="content">
                            <div
                                class="empty"
                                v-if="
                                    issueData.issueNewList !== undefined &&
                                    issueData.issueNewList.length === 0
                                ">
                                <el-empty
                                    :image-size="200"
                                    description="暂无新反馈" />
                            </div>
                            <el-scrollbar v-else max-height="auto">
                            </el-scrollbar>
                        </div>
                    </el-card>
                </el-col>
                <el-col :span="8">
                    <el-card class="issueDisplayCard">
                        <template #header>
                            <div class="card-header">
                                <span>重要反馈列表</span>
                            </div>
                        </template>
                        <div class="content">
                            <div
                                class="empty"
                                v-if="
                                    issueData.issueHighLevelList !==
                                        undefined &&
                                    issueData.issueHighLevelList.length === 0
                                ">
                                <el-empty
                                    :image-size="200"
                                    description="暂无重要反馈" />
                            </div>
                            <el-scrollbar
                                v-else
                                max-height="calc(100vh - 60px - 40px - 160px - 20px - 20.8px - 20px - 40px - 60px)"
                                :noresize="true">
                                <issue-card
                                    v-for="item in issueData.issueHighLevelList"
                                    style="margin-bottom: 8px"
                                    :issueId="item.issueId"
                                    :issueStatus="item.issueStatus"
                                    :issueTitle="item.issueTitle"
                                    :labels="item.labels" />
                            </el-scrollbar>
                        </div>
                    </el-card>
                </el-col>
                <el-col :span="8">
                    <el-card class="issueDisplayCard">
                        <template #header>
                            <div class="card-header">
                                <span>需要帮助反馈列表</span>
                            </div>
                        </template>
                        <div class="content">
                            <div
                                class="empty"
                                v-if="
                                    issueData.issueHighLevelList !==
                                        undefined &&
                                    issueData.issueHighLevelList.length === 0
                                ">
                                <el-empty
                                    :image-size="200"
                                    description="暂无需要帮助反馈" />
                            </div>
                            <el-scrollbar
                                v-else
                                max-height="calc(100vh - 60px - 40px - 160px - 20px - 20.8px - 20px - 40px - 60px)"
                                :noresize="true">
                                <issue-card
                                    v-for="item in issueData.issueNeedHelpList"
                                    style="margin-bottom: 8px"
                                    :issueId="item.issueId"
                                    :issueStatus="item.issueStatus"
                                    :issueTitle="item.issueTitle"
                                    :labels="item.labels" />
                            </el-scrollbar>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
        <custom-loading v-if="!issueData.isLoadingFinish" />
    </div>
</template>

<style scoped lang="less">
div.OverView,
div.data {
    width: 100%;
    height: 100%;
}

div.content {
    display: flex;
    flex-direction: column;
    gap: 12px;
    height: 100%;
    justify-content: center;
    div.empty {
        transform: translateY(-24px);
    }
}

.el-card.issueDisplayCard {
    min-height: 100%;
    max-height: calc(100vh - 60px - 40px - 160px - 20px - 40px - 5px);
}

.el-scrollbar {
    margin-bottom: 10px;
}

.el-col {
    text-align: center;
}
</style>
