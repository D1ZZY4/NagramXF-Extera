package tw.nekomimi.nekogram.settings;

import static org.telegram.messenger.LocaleController.getString;

import android.content.Context;
import android.view.View;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import org.telegram.messenger.MessagesController;
import org.telegram.messenger.R;
import org.telegram.messenger.browser.Browser;
import org.telegram.ui.Cells.TextSettingsCell;

import tw.nekomimi.nekogram.ui.cells.HeaderCell;

public class NagramExteraAboutActivity extends BaseNekoSettingsActivity {

    private int exteraHeaderRow;

    private int contentsSectionRow;
    private int exteraChannelRow;
    private int releaseChannelRow;
    private int discussionGroupRow;
    private int featuresTipsRow;
    private int contentsEndRow;

    private int creditsSectionRow;
    private int creditsFeaturesTipsRow;
    private int creditsNagramXFRow;
    private int creditsNagramXRow;
    private int creditsNagramRow;
    private int creditsEndRow;

    private int sourceCodeSectionRow;
    private int sourceCodeExteraRow;
    private int sourceCodeNagramXRow;
    private int sourceCodeNagramXFRow;
    private int sourceCodeAyugramRow;

    @Override
    protected void updateRows() {
        super.updateRows();

        exteraHeaderRow = addRow();

        contentsSectionRow = addRow();
        exteraChannelRow = addRow();
        releaseChannelRow = addRow();
        discussionGroupRow = addRow();
        featuresTipsRow = addRow();
        contentsEndRow = addRow();

        creditsSectionRow = addRow();
        creditsFeaturesTipsRow = addRow();
        creditsNagramXFRow = addRow();
        creditsNagramXRow = addRow();
        creditsNagramRow = addRow();
        creditsEndRow = addRow();

        sourceCodeSectionRow = addRow();
        sourceCodeExteraRow = addRow();
        sourceCodeNagramXRow = addRow();
        sourceCodeNagramXFRow = addRow();
        sourceCodeAyugramRow = addRow();
    }

    @Override
    protected String getActionBarTitle() {
        return getString(R.string.NagramExteraInfo);
    }

    @Override
    protected void onItemClick(View view, int position, float x, float y) {
        if (position == exteraChannelRow) {
            MessagesController.getInstance(currentAccount).openByUserName("NagramExteraOfficial", this, 1);
        } else if (position == releaseChannelRow) {
            MessagesController.getInstance(currentAccount).openByUserName("NagramExteraCloud", this, 1);
        } else if (position == discussionGroupRow) {
            MessagesController.getInstance(currentAccount).openByUserName("NagramExteraCommunity", this, 1);
        } else if (position == featuresTipsRow) {
            MessagesController.getInstance(currentAccount).openByUserName("NagramTips", this, 1);
        } else if (position == creditsFeaturesTipsRow) {
            MessagesController.getInstance(currentAccount).openByUserName("NagramTips", this, 1);
        } else if (position == creditsNagramXFRow) {
            MessagesController.getInstance(currentAccount).openByUserName("NagramX_Fork", this, 1);
        } else if (position == creditsNagramXRow) {
            MessagesController.getInstance(currentAccount).openByUserName("NagramX", this, 1);
        } else if (position == creditsNagramRow) {
            MessagesController.getInstance(currentAccount).openByUserName("nagram_channel", this, 1);
        } else if (position == sourceCodeExteraRow) {
            Browser.openUrl(getParentActivity(), "https://github.com/D1ZZY4/NagramXF-Extera");
        } else if (position == sourceCodeNagramXRow) {
            Browser.openUrl(getParentActivity(), "https://github.com/risin42/NagramX");
        } else if (position == sourceCodeNagramXFRow) {
            Browser.openUrl(getParentActivity(), "https://github.com/Keeperorowner/NagramXF");
        } else if (position == sourceCodeAyugramRow) {
            Browser.openUrl(getParentActivity(), "https://github.com/AyuGram/AyuGram4A");
        }
    }

    @Override
    protected BaseListAdapter createAdapter(Context context) {
        return new ListAdapter(context);
    }

    private class ListAdapter extends BaseListAdapter {

        public ListAdapter(Context context) {
            super(context);
        }

        @Override
        public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder, int position, boolean partial) {
            int viewType = holder.getItemViewType();
            if (viewType == TYPE_HEADER) {
                HeaderCell headerCell = (HeaderCell) holder.itemView;
                if (position == exteraHeaderRow) {
                    headerCell.setText(getString(R.string.NagramExtera));
                } else if (position == contentsSectionRow) {
                    headerCell.setText(getString(R.string.NagramExteraContents));
                } else if (position == creditsSectionRow) {
                    headerCell.setText(getString(R.string.NagramExteraCredits));
                } else if (position == sourceCodeSectionRow) {
                    headerCell.setText(getString(R.string.NagramExteraSourceCode));
                }
            } else if (viewType == TYPE_SETTINGS) {
                TextSettingsCell textCell = (TextSettingsCell) holder.itemView;
                if (position == exteraChannelRow) {
                    textCell.setTextAndValue(getString(R.string.NagramExteraChannel), "@NagramExteraOfficial", true);
                } else if (position == releaseChannelRow) {
                    textCell.setTextAndValue(getString(R.string.NagramExteraReleaseChannel), "@NagramExteraCloud", true);
                } else if (position == discussionGroupRow) {
                    textCell.setTextAndValue(getString(R.string.NagramExteraDiscussionGroup), "@NagramExteraCommunity", true);
                } else if (position == featuresTipsRow) {
                    textCell.setTextAndValue(getString(R.string.NagramExteraFeaturesTips), "@NagramTips", true);
                } else if (position == creditsFeaturesTipsRow) {
                    textCell.setTextAndValue(getString(R.string.NagramExteraFeaturesTips), "@NagramTips", true);
                } else if (position == creditsNagramXFRow) {
                    textCell.setTextAndValue(getString(R.string.NagramExteraSourceNagramXF), "@NagramX_Fork", true);
                } else if (position == creditsNagramXRow) {
                    textCell.setTextAndValue(getString(R.string.NagramX), "@NagramX", true);
                } else if (position == creditsNagramRow) {
                    textCell.setTextAndValue(getString(R.string.Nagram), "@nagram_channel", true);
                } else if (position == sourceCodeExteraRow) {
                    textCell.setTextAndValue(getString(R.string.NagramExtera), "GitHub", true);
                } else if (position == sourceCodeNagramXRow) {
                    textCell.setTextAndValue(getString(R.string.NagramX), "GitHub", true);
                } else if (position == sourceCodeNagramXFRow) {
                    textCell.setTextAndValue(getString(R.string.NagramExteraSourceNagramXF), "GitHub", true);
                } else if (position == sourceCodeAyugramRow) {
                    textCell.setTextAndValue(getString(R.string.NagramExteraSourceAyugram), "GitHub", false);
                }
            }
        }

        @Override
        public int getItemViewType(int position) {
            if (position == contentsEndRow || position == creditsEndRow) {
                return TYPE_SHADOW;
            } else if (position == exteraHeaderRow
                    || position == contentsSectionRow
                    || position == creditsSectionRow
                    || position == sourceCodeSectionRow) {
                return TYPE_HEADER;
            }
            return TYPE_SETTINGS;
        }
    }
}
