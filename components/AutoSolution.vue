<template>
  <div>
    <div v-if="!page.functionname">
      <p class="col-md-8">
        Autosolution is unsupported for this question, please manually submit a
        solution
      </p>
    </div>

    <div v-if="loaded && !!page.functionname">
      <p class="fs-5 col-md-8">
        Only Python Solutions are supported automatically here
      </p>

      <div class="container">
        <div class="row">
          <div class="col-8">
            <div class="input-group py-3">
              <textarea
                style="height: 400px; font-family: 'Baloo Bhaijaan 2', cursive"
                v-model="code"
                class="form-control bg-dark text-white border-0"
                aria-label="With textarea"
                id="submission"
              ></textarea>
            </div>
          </div>
          <div class="col-4">
            <div class="input-group py-3">
              <textarea
                style="height: 400px; font-family: 'Baloo Bhaijaan 2', cursive"
                v-model="output"
                class="form-control bg-secondary text-white border-0"
                aria-label="With textarea"
                disabled
                id="console"
              ></textarea>
            </div>
          </div>
        </div>
      </div>

      <button type="button" class="btn btn-primary btn-lg" v-on:click="run">
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
</template>

<style scoped>
submission {
  font-family: monospace;
}
</style>

<script>
export default {
  props: ["page"],
  data() {
    return {
      output: "",
      code: "# Paste your solution here",
      loaded: false,
      pyodide: null,
    };
  },
  methods: {
    initializePyodide: async function () {
      try {
        this.pyodide = await loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/",
        });

        // wait for pyodide ready
        await window.languagePluginLoader;
        // load pandas lib
        //await window.pyodide.loadPackage(["pandas", "scikit-learn"]);
      } catch (error) {
        this.errorMsg = error;
      }
    },
    run: async function main() {
      const { tests } = await this.$content(this.$props.page.path)
        .only(["tests"])
        .fetch();
      const { functionname } = await this.$content(this.$props.page.path)
        .only(["functionname"])
        .fetch();

      for (let i = 0; i < tests.length; i++) {
        this.pyodide
          .runPythonAsync(
            this.code + "\n" + String(functionname) + "(" + tests[i][0] + ")"
          )
          .then((output) => {
            let success = "";
            if (tests[i][1] == output) {
              success = "✔️";
            } else {
              success = "❌";
            }
            this.output =
              this.output +
              "INPUT: " +
              tests[i][0] +
              " // " +
              "OUTPUT: " +
              output +
              " // " +
              "EXPECTED: " +
              tests[i][1] +
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
  async mounted() {
    if (!!this.$props.page.functionname) {
      await this.initializePyodide();
      this.loaded = true;
    } else {
      this.loaded = true;
    }
  },
};
</script>
