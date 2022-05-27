<template>
  <div>
    <h1>Problems</h1>

    <div class="list-group px-5 mx-5 py-2">
      <NuxtLink
        v-for="question in questions"
        :key="question._id"
        :to="'/problems/' + question._id"
        class="list-group-item list-group-item-action d-flex gap-3 py-3 bg-dark text-white m-1 rounded-1"
        aria-current="true"
      >
        <div class="d-flex gap-2 w-100 justify-content-between">
          <div>
            <h6 class="mb-0">{{ question.questionName }}</h6>
            <p class="mb-0 opacity-75">
              {{ formatDate(question.createdAt) }}
            </p>
          </div>
          <small class="opacity-50 text-nowrap">{{
            question.questionDetails.creator
          }}</small>
        </div>
      </NuxtLink>
    </div>
  </div>
</template>

<script>
export default {
  // async fetch() {
  //   this.questions = await this.$content("questions")
  //     .only(["slug", "title", "createdAt", "creator"])
  //     .sortBy("createdAt", "asc")
  //     .fetch();
  // },
  data() {
    return { questions: null };
  },
  methods: {
    formatDate(date) {
      const options = { year: "numeric", month: "long", day: "numeric" };
      return (
        new Date(date).toLocaleDateString("en-GB", options) +
        " " +
        new Date(date).toLocaleTimeString("en-GB")
      );
    },
    async getQuestions() {
      let res = await this.$store.dispatch("getQuestions");
      this.questions = res.data;
    },
  },
  mounted() {
    this.getQuestions();
  },
};
</script>

<style></style>
