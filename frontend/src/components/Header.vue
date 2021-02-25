<template>
  <header class="header bg-site-primary" id="header">
      <p class="title text-center">{{ title }}</p>
  </header>
</template>

<script>
    export default {
        data: function() {
            return {
                title: "BHAVCOPY SEARCHIFIED"
            }
        }
    }
</script>

<style scoped>
    header {
        padding: 15px;
        box-shadow: 2px 2px 5px 1px #f1f1f1;
    }
    .title {
        color: #222;
        text-shadow: 1px 0 #888;
        letter-spacing: 1.1px;
        font-weight: bold;
        font-size: 2.4em;
        font-family: Arial;
    }
    @media (max-width: 576px) {
        header {
            padding: 10px;
            padding-bottom: 1px;
        }
        .title {
            font-size: 1em;
        }
    }
</style>
