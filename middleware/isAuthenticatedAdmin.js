export default function({ store, redirect }) {
  if (!store.state.auth.user.admin) {
    return redirect("/auth/login");
  }
}
