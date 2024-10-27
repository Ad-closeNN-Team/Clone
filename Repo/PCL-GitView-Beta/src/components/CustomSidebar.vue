<script setup>
import { ref } from "vue";
import SidebarButtonGroup from "./SidebarButtonGroup.vue";
</script>

<template>
    <el-scrollbar class="sidebar">
        <sidebar-button-group title="欢迎！">
            <el-link :type="$router.currentRoute.value['path'] === '/Intro' ? 'primary' : 'default'" @click="refetchPath()" href="/#/Intro">
                项目简介
            </el-link>
        </sidebar-button-group>
        <sidebar-button-group title="Issues 大区">
            <el-link :type="$router.currentRoute.value['path'] === '/IssuesOverview' ? 'primary' : 'default'" @click="refetchPath()" href="/#/IssuesOverview">
                总览
            </el-link>
            <el-link :type="$router.currentRoute.value['path'] === '/IssuesLabel' ? 'primary' : 'default'" @click="refetchPath()" href="/#/IssuesLabel">
                标签分布
            </el-link>
            <el-link :type="$router.currentRoute.value['path'] === '/IssuesChangeTrend' ? 'primary' : 'default'" @click="refetchPath()" href="/#/IssuesChangeTrend">
                变化趋势
            </el-link>
        </sidebar-button-group>   
        <sidebar-button-group title="Discussions 大区">
            <el-link :type="$router.currentRoute.value['path'] === '/DiscOverview' ? 'primary' : 'default'" @click="refetchPath()" href="/#/DiscOverview">
                总览
            </el-link>
            <el-link :type="$router.currentRoute.value['path'] === '//DiscCatgory' ? 'primary' : 'default'" @click="refetchPath()" href="/#//DiscCatgory">
                分区预览
            </el-link>
            <el-link :type="$router.currentRoute.value['path'] === '//DiscChangeTrend' ? 'primary' : 'default'" @click="refetchPath()" href="/#//DiscChangeTrend">
                变化趋势
            </el-link>
        </sidebar-button-group> 
    </el-scrollbar>
</template>

<style scoped lang="less">
.sidebar {
    width: 220px;
    .el-link {
        margin-left: 36px;
        width: max-content;
    }
}
</style>
