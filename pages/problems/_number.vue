<template>
  <main>
    <div class="accordion accordion-flush" id="accordionFlushExample">
      <div class="accordion-item bg-dark">
        <h2 class="accordion-header" id="flush-headingOne">
          <button
            class="accordion-button collapsed bg-dark text-white"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#flush-collapseOne"
            aria-expanded="false"
            aria-controls="flush-collapseOne"
          >
            <h1>Question {{ $route.params.number }}</h1>
          </button>
        </h2>
        <div
          id="flush-collapseOne"
          class="accordion-collapse collapse show"
          aria-labelledby="flush-headingOne"
        >
          <div class="accordion-body">
            <nuxt-content :document="page" />
          </div>
        </div>
      </div>
      <div class="accordion-item bg-dark">
        <h2 class="accordion-header" id="flush-headingTwo">
          <button
            class="accordion-button collapsed bg-dark text-white"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#flush-collapseTwo"
            aria-expanded="false"
            aria-controls="flush-collapseTwo"
          >
            <h1>Submit Solution</h1>
          </button>
        </h2>
        <div
          id="flush-collapseTwo"
          class="accordion-collapse collapse"
          aria-labelledby="flush-headingTwo"
        >
          <div class="accordion-body">
            <div v-if="loaded">
              <p class="fs-5 col-md-8">
                Submit your solution here.
                <b>Only Python Solutions are supported automatically here </b>
                and you can attach alternative solutions at the bottom for
                review
              </p>

              <div class="input-group py-3">
                <textarea
                  style="
                    height: 500px;
                    font-family: 'Baloo Bhaijaan 2', cursive;
                  "
                  v-model="code"
                  class="form-control bg-dark text-white border-0"
                  aria-label="With textarea"
                  id="submission"
                ></textarea>
              </div>

              <div class="input-group py-3">
                <textarea
                  style="
                    height: 300px;
                    font-family: 'Baloo Bhaijaan 2', cursive;
                  "
                  v-model="output"
                  class="form-control bg-secondary text-white border-0"
                  aria-label="With textarea"
                  disabled
                  id="console"
                ></textarea>
              </div>

              <button
                type="button"
                class="btn btn-primary btn-lg"
                v-on:click="run"
              >
                Run
              </button>

              <!--
              <button
                type="button"
                class="btn btn-success btn-lg"
                v-on:click="submit"
              >
                Submit
              </button> -->
            </div>

            <div v-if="!loaded">
              <div class="d-flex justify-content-center">
                <div class="spinner-border" role="status">
                  <span class="visually-hidden">Loading...</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <hr class="my-5" />

    <div class="row g-5">
      <div class="col-md-6">
        <h2>Stuck?</h2>
        <p>
          {{ page.hint }}
        </p>
      </div>

      <div class="col-md-6">
        <h2>Details</h2>
        <p>Details regarding the question</p>
        <table class="table table-dark table-striped">
          <tbody>
            <tr>
              <td>Created</td>
              <td>{{ formatDate(page.createdAt) }}</td>
            </tr>
            <tr>
              <td>Updated</td>
              <td>{{ formatDate(page.updatedAt) }}</td>
            </tr>
            <tr>
              <td>Original Deadline</td>
              <td>{{ page.deadline }}</td>
            </tr>
            <tr>
              <td>Made by</td>
              <td>{{ page.creator }}</td>
            </tr>
            <tr>
              <td>Function Name</td>
              <td>{{ page.functionname + "()" }}</td>
            </tr>
            <tr>
              <td>Path</td>
              <td>{{ page.path }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  ssr: false,
  data() {
    return {
      code: "# Paste your solution here",
      pyodide: null,
      output: "",
      loaded: false,
      tests: [],
    };
  },
  async mounted() {
    this.pyodide = await loadPyodide({
      indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/",
    });
    this.loaded = true;
  },
  async asyncData({ params, $content }) {
    const page = await $content("questions/" + params.number).fetch();
    return {
      page,
    };
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
    run: async function main() {
      const { tests } = await this.$content("questions/1")
        .only(["tests"])
        .fetch();

      const { functionname } = await this.$content("questions/1")
        .only(["functionname"])
        .fetch();

      this.tests = tests;

      for (let i = 0; i < this.tests.length; i++) {
        this.pyodide
          .runPythonAsync(
            this.code +
              "\n" +
              String(functionname) +
              "(" +
              this.tests[i][0] +
              ")"
          )
          .then((output) => {
            let success = "";
            if (this.tests[i][1] == output) {
              success = "✔️";
            } else {
              success = "❌";
            }

            this.output =
              this.output +
              "INPUT: " +
              this.tests[i][0] +
              " // " +
              "OUTPUT: " +
              output +
              " // " +
              "EXPECTED: " +
              this.tests[i][1] +
              " | " +
              success +
              "\n";

            var textarea = document.getElementById("console");
            textarea.scrollTop = textarea.scrollHeight;
          })

          .catch((err) => (this.output = err));
      }

      this.output = this.output + "\n";
    },
  },
};
</script>

<style>
.accordion-body {
  background-color: #343a40;
}
</style>
