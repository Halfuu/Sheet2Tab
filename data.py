import mido
import pandas as pd
import os

class Sheet2TabDataset(Dataset):

    ## creates a dataset from given tabs and sheet music. If sheet music not provided,
    ## then creates the sheet music from the guitar tabs, and forms a new directory with the resulting sheet music in it
    ## number of tabs and sheets should be the same
    def __init__(self, tab_dir, tabs_file, sheet_dir=None, sheets_file=None):
        self.tab_dir = tab_dir 
        self.tab_labels = pd.read_csv(tabs_file)## TODO: labels for tabs (use pd most likely)
        self.sheet_dir = sheet_dir ## handle case where sheet dne
        self.sheet_labels = pd.read_csv(sheets_file) ## TODO: labels (?) for sheet

        if not self.sheet_dir:
            pass
            ## do something
        if not self.sheet_labels:
            pass
            ## do something

    def __len__(self):
        return len(self.tab_dir)
    
    def __getitem__(self, idx):
        tab_path = os.path.join(self.tab_dir, self.tab_labels.iloc([idx, 0]))
        tab_label = self.tab_labels.iloc[idx, 1]
        tab = #TODO

        sheet_path = os.path.join(self.sheet_dir.iloc, self.sheet_labels.iloc[idx, 1])
        sheet_label = self.tab_labels.iloc[idx, 1]

        sheet = #TODO

        sample = {"sheet music": sheet, "guitar tab": tab}
#TODO: look into guitarset and lakh midi dataset
# https://guitarset.weebly.com/
# https://colinraffel.com/projects/lmd/