import { createWebHistory, createRouter } from "vue-router";

const routes =  [
  {
    path: "/",
    alias: "/movies",
    name: "movies",
    component: () => import("./components/MoviesList")
  },
  {
    path: "/movies/:id",
    name: "movie-details",
    component: () => import("./components/Movie")
  },
  {
    path: "/add_movie",
    name: "add_movie",
    component: () => import("./components/AddMovie")
  },
  /*{
      path: "/add_review",
      name: "add_review",
      component: () => import("./components/AddReview")
  },*/
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;