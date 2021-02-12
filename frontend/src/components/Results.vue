<template>
<div class="container">

    <div class="row stock-name">
        <div class="col-md-12"></div>

        <!-- Name of the stock -->
        <h2>{{ result.name }}</h2>

    </div>

    <div class="row">

        <div class="table-responsive">

        <table class="table">
            <caption>Prices are in Rs.</caption>

            <thead class="thead thead-dark">
                <tr>
                    <!-- Result Key: Date -->
                    <th>{{ result.records[0][0].toUpperCase() }}</th>

                    <!-- Rest of the numerical result keys -->
                    <th v-for="key in result.records[0].slice(1,)" class="text-center">{{ key.toUpperCase() }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="record in result.records[1]">
                    <!-- dd-mm-yyyy of the record -->
                    <td>{{ record[0] }}</td>

                    <!-- numerical values -->
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
    .stock-name {
        margin-top: 50px;
        padding: 10px;
    }
</style>
