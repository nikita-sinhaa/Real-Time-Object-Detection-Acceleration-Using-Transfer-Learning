
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity axi_bbox_filter is
    Port (
        clk       : in  STD_LOGIC;
        resetn    : in  STD_LOGIC;
        s_conf    : in  STD_LOGIC_VECTOR(15 downto 0);
        s_valid   : in  STD_LOGIC;
        m_keep    : out STD_LOGIC;
        m_valid   : out STD_LOGIC
    );
end axi_bbox_filter;

architecture Behavioral of axi_bbox_filter is
    signal internal_keep : STD_LOGIC;
begin

    bbox_inst: entity work.bbox_filter
        port map (
            clk    => clk,
            conf   => s_conf,
            enable => s_valid,
            keep   => internal_keep
        );

    m_keep <= internal_keep;
    m_valid <= s_valid and internal_keep;

end Behavioral;
