import { createRouter, createWebHashHistory } from "vue-router";

const gen403Routes = (pathList) => {
    return pathList.map((path) => ({
        path: path,
        component: () => import("../views/403.vue"),
    }));
};

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: "/",
            component: () => import("../views/HomeView.vue"),
        },
        {
            path: "/IssuesOverview",
            component: () => import("../views/issues/OverView.vue"),
        },
        // 403 (Not Complete Pages) (Only For Deploy Environment)
        ...gen403Routes([
            "/Intro",
            "/IssuesLabel",
            "/IssuesChangeTrend",
            "/DiscOverview",
            "/DiscCatgory",
            "/DiscChangeTrend",
        ]),
        // 404
        {
            path: "/:pathMatch(.*)*",
            component: () => import("../views/404.vue"),
        },
    ],
});

export default router;
