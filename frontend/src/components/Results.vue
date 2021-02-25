<template>
<div class="container">

    <div v-if="result.name" class="row stock-name">
        <div class="col-md-9 col-8">
            <div class="row">
                <!-- Name of the stock -->
                <span>{{ result.name }}</span>
            </div>
        </div>
        <div class="col-md-3 col-4 download">
                <button type="button" class="btn bg-site-primary action_btn float-right" v-on:click="downloadCSVData">
                  DOWNLOAD CSV
                </button>
        </div>

    </div>

    <div v-if="!result.name" class="row stock-name">
        <div class="col-md-12"></div>

        <!-- Name of the stock -->
        <h4>Latest BSE Highlights</h4>

    </div>

    <div class="row">

        <div class="col">
        <div class="table-responsive">

        <table class="table">
            <caption>Prices are in Rs.</caption>

            <thead class="thead bg-offwhite">
                <tr>
                    <!-- Result Key: Date -->
                    <th>{{ result.records[0][0].toUpperCase() }}</th>

                    <!-- Rest of the numerical result keys -->
                    <th v-for="key, index in result.records[0].slice(1,)" :key="index" class="text-center">{{ key.toUpperCase() }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="record, index in result.records[1]" :key="index">
                    <!-- dd-mm-yyyy of the record -->
                    <th>{{ record[0] }}</th>

                    <!-- numerical values -->
                    <td v-for="value, index in record.slice(1,)" :key="index" class="text-center">{{ value }}</td>
                </tr>
            </tbody>
        </table>

        </div>
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
        methods: {
            // Ref: https://stackoverflow.com/a/58293004/3860168

            downloadCSVData: function() {
                let csv = 'Date,Code,Open,High,Low,Close\n';
                this.result.records[1].forEach((row) => {
                    csv += row.join(',');
                    csv += "\n";
                });

                const anchor = document.createElement('a');
                anchor.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv);
                anchor.target = '_blank';
                anchor.download = 'EQ-' + this.result.name + '.csv';
                anchor.click();
            }
        }
    }
</script>

<style scoped>
    .stock-name {
        margin-top: 50px;
        padding: 10px;
        font-size: 28px;
        font-weight: bolder;
        margin-left: 0;
    }
    .bg-offwhite {
        background: #f2f2f2;
    }
    .download button {
        box-shadow: 2px 2px 5px 1px #f1f1f1;
    }
    @media (max-width: 576px) {
        .stock-name {
            font-size: 12px;
        }
        .download button {
            font-size: 8px;
            padding: 5px;
        }
    }
</style>
