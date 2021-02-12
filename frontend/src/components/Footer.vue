<template>
    <footer class="footer">
        <p class="copyleft text-center">{{ copyleft }}</p>
    </footer>
</template>

<script>
    export default {
        data: function() {
            return {
                copyleft: "Copyleft 2021 Bhavcopy Searchified"
            }
        }
    }
</script>

<style scoped>
    footer {
        background: #222;
        padding: 10px;
        box-shadow: 2px 2px 5px 1px #f1f1f1;
        position: fixed;
        bottom: 0;
        width: 100%;
    }
    .copyleft {
        color: lightgreen;
        font-size: 1em;
    }
</style>
