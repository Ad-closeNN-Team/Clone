<script setup>
import LogoCard from "@/components/LogoCard.vue";
import { reactive } from "vue";

const emit = defineEmits(["logoClick"]);

const handleClick = () => {
    emit("logoClick");
};

const rea = reactive({
    theme: null,
});
// Theme Change Detector
const matchTheme = (e) => {
    if (e.matches) {
        rea.theme = "light";
    } else {
        rea.theme = "dark";
    }
};
window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", matchTheme);
matchTheme(window.matchMedia("(prefers-color-scheme: dark)"));
</script>

<template>
    <div class="custom-header">
        <div class="logo">
            <logo-card
                :shadow="false"
                style="
                    transform: translateX(-330px) scale(0.08);
                    cursor: pointer;
                "
                id="logoc"
                @click="handleClick()" />
        </div>
        <h1 style="cursor: pointer" @click="$router.push('/')">PCL GitView</h1>
        <el-tag :effect="rea.theme" type="warning">先遣体验版本</el-tag>
        <el-tag :effect="rea.theme" type="warning">v2.0.2</el-tag>
    </div>
</template>

<style scoped lang="less">
div.custom-header {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    div.logo {
        width: 50px;
    }
    h1 {
        margin-left: 16px;
        margin-right: 8px;
    }
}
</style>
