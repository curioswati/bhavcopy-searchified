<template>
    <footer class="footer">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <p class="copyleft text-center float-left ">{{ copyleft }}</p>
                </div>
                <div class="col-md-4"></div>
                <div class="col-md-4">
                    <ul class="list-unstyled list-inline float-right">
                        <li>
                        <a href="https://github.com/curioswati/bhavcopy-searchified" aria-hidden="true" role="link" target="_blank">
                            <font-awesome-icon :icon="['fab', 'github']" class="fa" />
                        </a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
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
        padding: 15px;
        box-shadow: 2px 2px 5px 1px #f1f1f1;
        position: fixed;
        bottom: 0;
        width: 100%;
    }
    .copyleft {
        color: lightgreen;
        font-size: 1em;
    }
    .fa {
        color: lightgreen;
        font-size: 25px;
    }
    .fa:hover {
        color: white;
    }
    footer p, footer ul {
        margin-bottom: 0;
    }
</style>
