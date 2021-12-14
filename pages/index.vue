<template>
  <div>
    <h1>Problems</h1>
    <ul>
      <li v-for="article of articles" :key="article.slug">
        <NuxtLink :to="'/problems/' + article.slug">
          <div>
            <h2>{{ article.title }}</h2>
          </div>
        </NuxtLink>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  async asyncData({ $content, params }) {
    const articles = await $content('questions', params.slug)
      .only(['title', 'slug'])
      .sortBy('createdAt', 'asc')
      .fetch();

    return {
      articles,
    };
  },
};
</script>

<style></style>
