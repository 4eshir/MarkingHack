import csv

class CsvWizard:

    @staticmethod
    def ParseCsv(filepath, delimiter, exportCols, startRow = 0):
        result = []
        for temp in exportCols:
            result.append([])

        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
            rc = 0
            for row in reader:
                if rc >= startRow:
                    for i in range(len(row)):
                        for j in range(len(exportCols)):
                            if i == exportCols[j]:
                                result[j].append(row[i])
                rc += 1

        return result