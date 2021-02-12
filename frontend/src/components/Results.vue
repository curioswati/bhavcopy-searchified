<template>
<div class="container">

    <div class="row">
        <div class="col-md-12" style="height:10vh;"></div>
        <h2>{{ result.name }}</h2>
    </div>

    <div class="row">

        <div class="table-responsive">
        <table class="table table">
            <caption>Prices are in Rs.</caption>

            <thead class="thead thead-dark">
                <tr>
                    <th>{{ result.records[0][0].toUpperCase() }}</th>
                    <th v-for="key in result.records[0].slice(1,)" class="text-center">{{ key.toUpperCase() }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="record in result.records[1]">
                    <td>{{ record[0] }}</td>
                    <td v-for="value in record.slice(1,)" class="text-center">{{ value }}</td>
                </tr>
            </tbody>
        </table>
        </div>

    </div>
</div>
</template>

<script>
    export default {
        name: "Results",
        props: {
            result: {
                type: Object,
                required: true
            }
        },
    }
</script>

<style scoped>
</style>
