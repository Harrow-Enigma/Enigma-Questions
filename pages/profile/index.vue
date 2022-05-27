<template>
  <div>
    Hello dear <b style="color:red">{{ getUserInfo.fullname }}</b> you're in
    profile page
    <hr />
    This is your information:
    <br /><br />
    <table class="table">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">FullName</th>
          <th scope="col">Email</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ getUserInfo.id }}</td>
          <td>{{ getUserInfo.fullname }}</td>
          <td>{{ getUserInfo.email }}</td>
        </tr>
      </tbody>
    </table>

    <p v-if="getUserInfo.admin">You are an admin</p>
    <p v-if="!getUserInfo.admin">You aren't an admin</p>
  </div>
</template>

<script>
export default {
  middleware: "isAuthenticated",
  data() {
    return {
      newQuestion: {
        questionName: "",
        questionNumber: "",
        questionText: "",
        questionDetails: {
          deadline: "",
          creator: ""
        }
      }
    };
  },
  methods: {
    addQuestion() {
      this.$http.post("/api/questions", this.newQuestion).then(response => {
        this.newQuestion = {
          questionName: "",
          questionNumber: "",
          questionText: "",
          questionDetails: {
            deadline: "",
            creator: ""
          }
        };
      });
    }
  },
  computed: {
    getUserInfo() {
      return this.$store.getters.getUserInfo;
    }
  }
};
</script>

<style>
* {
  color: white;
}
</style>
