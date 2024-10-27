<script setup>
defineProps({
    title: String,
});
</script>

<template>
    <div class="s-b-group">
        <h4>{{ title }}</h4>
        <div class="content">
            <slot></slot>
        </div>
    </div>
</template>

<style scoped lang="less">
div.s-b-group {
    margin-bottom: 36px;
    h4 {
        margin-bottom: 16px;
    }
    .content {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        gap: 12px;
    }
}
</style>
