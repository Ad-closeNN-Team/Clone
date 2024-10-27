<script setup>
import { RouterView } from "vue-router";
import CustomHeader from "./components/CustomHeader.vue";
import CustomSidebar from "./components/CustomSidebar.vue";
const year = new Date().getFullYear();

const open_close_sidebar = () => {
    document.querySelector(".el-aside").classList.toggle("hide");
};
</script>

<template>
    <el-container class="container-main">
        <el-header>
            <custom-header @logoClick="open_close_sidebar" />
        </el-header>
        <el-container>
            <el-aside>
                <custom-sidebar />
            </el-aside>
            <el-container>
                <el-main>
                    <Suspense>
                        <RouterView />
                    </Suspense>
                </el-main>  
                <el-footer height="40px">
                    <span>
                        Copyright &copy;{{
                            year <= 2024 ? year : `2024-${year}`
                        }}
                        <el-link
                            class="pcl-link"
                            href="https://github.com/PCL-Community"
                            target="_blank">
                            <span>PCL-Community</span>
                        </el-link>
                        , All Rights Reserved.
                    </span>
                </el-footer>
            </el-container>
        </el-container>
    </el-container>
</template>

<style scoped lang="less">
.el-container.container-main {
    width: 100%;
    min-height: 100vh;
    .el-header {
        display: flex;
        align-items: center;
        overflow: hidden;
        border-bottom: 1px solid var(--color-border);
    }
    .el-aside {
        width: 300px;
        display: flex;
        justify-content: center;
        overflow: hidden;
        border-right: 1px solid var(--color-border);
        transition: width 0.3s ease-in-out;
        .sidebar {
            display: block;
        }
        &.hide {
            width: 0;
            border: none;
            .sidebar {
                display: none;
            }
        }
    }
    .el-main {
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }
    .el-footer {
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        border-top: 1px solid var(--color-border);
    }
}

.el-link.pcl-link {
    color: inherit;
    font-size: inherit;
    font-weight: inherit;
    font-family: inherit;
    line-height: inherit;
    vertical-align: baseline;
    &:hover {
        color: var(--el-link-hover-text-color);
    }
}
</style>
