export const getters = {
  isAuthenticated(state) {
    return state.auth.loggedIn; // auth object as default will be added in vuex state, when you initialize nuxt auth
  },
  isAuthenticatedAdmin(state) {
    return state.auth.user.admin; 
  },
  getUserInfo(state) {
    return state.auth.user;
  }
};
