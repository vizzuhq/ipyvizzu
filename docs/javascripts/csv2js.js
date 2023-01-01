class Csv2Js {
  static csv(csv, dimensions) {
    return new Promise((resolve, reject) => {
      if (!dimensions) {
        dimensions = [];
      }
      const detectedDimensions = {};
      const data = { series: [], records: [] };
      // eslint-disable-next-line no-undef
      d3.csv(
        csv,
        (row) => {
          const record = [];
          const keys = Object.keys(row);
          for (const key of keys) {
            const numValue = +row[key];
            if (!isNaN(numValue)) {
              record.push(numValue);
            } else {
              record.push(row[key]);
              detectedDimensions[key] = true;
            }
          }
          data.records.push(record);
          return record;
        },
        (error, rows) => {
          if (error) {
            return reject(error);
          }
          for (let i = 0; i < rows.columns.length; i++) {
            const key = rows.columns[i];
            const series = {
              name: key,
              type:
                dimensions.includes(key) || detectedDimensions[key]
                  ? "dimension"
                  : "measure",
            };
            data.series.push(series);
          }
          return resolve(data);
        }
      );
    });
  }
}

export default Csv2Js;
