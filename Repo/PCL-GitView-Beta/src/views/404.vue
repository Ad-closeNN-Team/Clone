<script setup>
import { ref } from "vue";

const btnColor = ref(null);
const matchTheme = (e) => {
    if (e.matches) {
        btnColor.value = "#0665D2";
    } else {
        btnColor.value = "#0c72e7";
    }
};
window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", matchTheme);
matchTheme(window.matchMedia("(prefers-color-scheme: dark)"));
</script>

<template>
    <el-result
        icon="error"
        title="404 Not Found"
        sub-title="你所查找的页面不存在">
        <template #extra>
            <el-button
                type="primary"
                :color="btnColor"
                @click="$router.go(-1)">
                返回
            </el-button>
        </template>
    </el-result>
</template>
