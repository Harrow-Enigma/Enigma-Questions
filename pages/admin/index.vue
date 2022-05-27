<template>
  <div>
    Hello dear <b style="color:red">{{ getUserInfo.fullname }}</b> you're in
    admin page
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

    <!-- a form to add a new question to db -->
    <form @submit.prevent="createQuestion">
      <div class="form-group">
        <label for="question">Question Name</label>
        <input
          type="text"
          class="form-control"
          id="question"
          v-model="newQuestion.questionName"
        />
      </div>
      <div class="form-group">
        <label for="slug">questionNumber</label>
        <input
          type="number"
          class="form-control"
          id="slug"
          v-model="newQuestion.questionNumber"
        />
      </div>
      <div class="form-group">
        <label for="question">Question Text</label>
        <input
          type="text"
          class="form-control"
          id="question"
          v-model="newQuestion.questionText"
        />
      </div>
      <div class="form-group">
        <label for="question">Deadline</label>
        <input
          type="date"
          class="form-control"
          id="question"
          v-model="newQuestion.questionDetails.deadline"
        />
      </div>
      <div class="form-group">
        <label for="question">Creator</label>
        <input
          type="text"
          class="form-control"
          id="question"
          v-model="newQuestion.questionDetails.creator"
        />
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>

    <p v-if="!getUserInfo.admin">You aren't an admin</p>
  </div>
</template>

<script>
export default {
  middleware: "isAuthenticatedAdmin",
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
    // send a post request to add a new question to db using axios
    async createQuestion() {
      const request = await this.$axios.$post(
        "/api/admin/createQuestion",
        this.newQuestion
      );
      this.request = request;
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
